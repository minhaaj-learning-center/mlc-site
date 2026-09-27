const menu = document.querySelector('[data-mobile-menu]');

if (menu) {
  const trigger = menu.querySelector('summary');
  const syncExpandedState = () => {
    const expanded = Boolean(menu.open);
    trigger?.setAttribute('aria-expanded', String(expanded));
    trigger?.setAttribute('aria-label', `${expanded ? 'Close' : 'Open'} navigation menu`);
  };
  const closeMenu = () => {
    menu.removeAttribute('open');
    syncExpandedState();
  };

  syncExpandedState();
  menu.addEventListener('toggle', syncExpandedState);

  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.open) {
      closeMenu();
      trigger?.focus();
    }
  });

  const desktopQuery = window.matchMedia('(min-width: 768px)');
  const handleDesktopChange = (event) => {
    if (event.matches) closeMenu();
  };

  if (desktopQuery.addEventListener) {
    desktopQuery.addEventListener('change', handleDesktopChange);
  } else {
    desktopQuery.addListener(handleDesktopChange);
  }
}

document.querySelectorAll('[data-current-year]').forEach((year) => {
  year.textContent = String(new Date().getFullYear());
});
