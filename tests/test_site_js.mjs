import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import vm from 'node:vm';

const source = await readFile(new URL('../assets/js/site.js', import.meta.url), 'utf8');

let failures = 0;
function test(name, callback) {
  try {
    callback();
    console.log(`ok - ${name}`);
  } catch (error) {
    failures += 1;
    console.error(`not ok - ${name}`);
    console.error(error);
  }
}

class EventTarget {
  constructor() { this.listeners = new Map(); }
  addEventListener(type, listener) {
    const listeners = this.listeners.get(type) ?? [];
    listeners.push(listener);
    this.listeners.set(type, listeners);
  }
  dispatch(type, event = {}) {
    for (const listener of this.listeners.get(type) ?? []) listener(event);
  }
}

function createHarness({ legacyMediaQuery = false, year = 2031 } = {}) {
  const trigger = new EventTarget();
  trigger.attributes = new Map([['aria-label', 'Open navigation menu']]);
  trigger.focused = false;
  trigger.setAttribute = (name, value) => trigger.attributes.set(name, value);
  trigger.focus = () => { trigger.focused = true; };

  const link = new EventTarget();
  const menu = new EventTarget();
  menu.open = false;
  menu.querySelector = (selector) => selector === 'summary' ? trigger : null;
  menu.querySelectorAll = (selector) => selector === 'a' ? [link] : [];
  menu.removeAttribute = (name) => { if (name === 'open') menu.open = false; };

  const yearNode = { textContent: '2026' };
  const documentElement = { classList: { add() {} } };
  const document = new EventTarget();
  document.documentElement = documentElement;
  document.querySelector = (selector) => selector === '[data-mobile-menu]' ? menu : null;
  document.querySelectorAll = (selector) => selector === '[data-current-year]' ? [yearNode] : [];

  const mediaQuery = new EventTarget();
  mediaQuery.addListener = (listener) => { mediaQuery.legacyListener = listener; };
  if (legacyMediaQuery) mediaQuery.addEventListener = undefined;

  class ControlledDate extends Date {
    constructor(...args) { super(...(args.length ? args : [`${year}-01-01T00:00:00Z`])); }
    getFullYear() { return year; }
  }

  vm.runInNewContext(source, {
    document,
    window: { matchMedia: () => mediaQuery },
    Date: ControlledDate,
  });
  return { document, link, mediaQuery, menu, trigger, yearNode };
}

test('menu state keeps expanded state and action label synchronized', () => {
  const harness = createHarness();
  assert.equal(harness.trigger.attributes.get('aria-expanded'), 'false');
  assert.equal(harness.trigger.attributes.get('aria-label'), 'Open navigation menu');
  harness.menu.open = true;
  harness.menu.dispatch('toggle');
  assert.equal(harness.trigger.attributes.get('aria-expanded'), 'true');
  assert.equal(harness.trigger.attributes.get('aria-label'), 'Close navigation menu');
  harness.document.dispatch('keydown', { key: 'Escape' });
  assert.equal(harness.menu.open, false);
  assert.equal(harness.trigger.attributes.get('aria-label'), 'Open navigation menu');
  assert.equal(harness.trigger.focused, true);
});

test('responsive cleanup supports the legacy MediaQueryList listener API', () => {
  const harness = createHarness({ legacyMediaQuery: true });
  harness.menu.open = true;
  assert.equal(typeof harness.mediaQuery.legacyListener, 'function');
  harness.mediaQuery.legacyListener({ matches: true });
  assert.equal(harness.menu.open, false);
});

test('current year hooks use the controlled current year', () => {
  const harness = createHarness({ year: 2042 });
  assert.equal(harness.yearNode.textContent, '2042');
});

if (failures) process.exitCode = 1;
