---
title: 'Modernize the MLC website'
type: 'feature'
ticket: ''
created: '2026-09-26'
status: 'blocked'
route: 'full'
route_source: 'auto'
baseline_revision: 'NO_VCS'
review: 'thorough'
review_source: 'auto'
lenses_ran: ['blind-hunter', 'edge-case-hunter', 'verification-gap']
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/specs/spec-mlc-modernization/SPEC.md'
  - '{project-root}/_bmad-output/specs/spec-mlc-modernization/content-inventory.md'
  - '{project-root}/_bmad-output/specs/spec-mlc-modernization/conventions.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** MLC's current site is visually dated, mobile-heavy visitors must work too hard to understand its programs, and registration depends on an image-led presentation.

**Approach:** Build one cohesive, mobile-first static website with Home, Programs, and About pages. Preserve the approved source content while presenting it through a modern Islamic institutional design and a registration-first HTML/CSS hero.

## Boundaries & Constraints

**Always:** Use semantic vanilla HTML, minimal vanilla JavaScript, and Tailwind-generated static CSS. Make registration prominent in the first mobile viewport; use the confirmed Google Form. Preserve the content inventory, Arabic text direction, shared contact information, accessible navigation, visible focus states, readable contrast, and static-safe relative paths. Keep source and build configuration suitable for GitHub and GoDaddy-managed domain/CDN delivery.

**Never:** Add a framework, server runtime, CMS, authentication, payment flow, on-site registration form, Tailwind browser runtime, image-based essential text, unsupported institutional claims, or pages beyond Home, Programs, and About.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Primary registration | Visitor activates any Register action | Confirmed Google Form opens safely | Link remains a normal visible anchor if JavaScript is unavailable |
| Mobile navigation | Narrow viewport with menu closed | Button exposes three page links and accurate expanded state | Links remain available when JavaScript is unavailable |
| Arabic quotation | Mixed English and Arabic content | Arabic renders right-to-left without disturbing surrounding layout | Semantic `lang` and `dir` attributes isolate bidirectional text |
| Static hosting | Site served from domain root or local static server | Pages, stylesheet, and script resolve with relative URLs | No route rewriting or server runtime is required |

</frozen-after-approval>

## Code Map

- `package.json` -- npm metadata and Tailwind CLI build/watch scripts; use Tailwind v4 CLI to emit zero-runtime CSS.
- `src/input.css` -- Tailwind import, green/gold theme tokens, shared base styling, and small reusable component rules.
- `assets/css/styles.css` -- generated production stylesheet; do not hand-edit.
- `assets/js/site.js` -- progressive mobile-menu state only; HTML remains navigable without it.
- `index.html` -- registration-first hero, mission, curriculum overview, community commitments, and contact CTA.
- `programs.html` -- Weekend School, Knowledge Retreats, and complete course-topic content.
- `about.html` -- MLC purpose, clear-path narrative, Arabic hadith with translation, teaching focus, and accessibility commitment.
- `.gitignore` -- exclude dependencies while retaining deployable static assets.

## Tasks & Acceptance

**Execution:**
- [x] `package.json`, `.gitignore`, `src/input.css` -- establish the minimal Tailwind v4 CLI pipeline, theme, and deployable generated-CSS convention.
- [x] `assets/js/site.js` plus shared page header/footer markup -- implement progressive, keyboard-accessible navigation and consistent registration/contact actions.
- [x] `index.html` -- build the semantic mobile-first homepage and HTML/CSS hero from CAP-1 and CAP-2.
- [x] `programs.html` -- present all approved program and course content in a scannable mobile-first hierarchy for CAP-3.
- [x] `about.html` -- preserve the approved narrative and bidirectional quotation for CAP-4.
- [x] `assets/css/styles.css` and all pages -- compile production CSS, validate internal/external links, and inspect responsive/accessibility behavior.

**Acceptance Criteria:**
- Given a phone-width viewport, when Home loads, then MLC's purpose and a working Register action appear in the initial viewport without flyer imagery or horizontal scrolling.
- Given any page at phone or desktop width, when navigation is used by touch or keyboard, then Home, Programs, About, and Register are reachable with visible focus and accurate state.
- Given the three-page content inventory, when the finished pages are reviewed, then every load-bearing item appears on its assigned page without new religious or program claims.
- Given JavaScript is disabled, when a visitor browses the site, then core content, page links, registration, and contact actions remain usable.
- Given a static HTTP server, when all three pages load, then local assets resolve, production CSS contains no Tailwind browser dependency, and there are no broken internal links.

## Implementation Notes

- Completed the three-page static site and shared registration/contact/navigation surfaces.
- Added synchronized `aria-expanded` state to the progressive `<details>` mobile menu while retaining usable links without JavaScript.
- Added `tests/test_static_site.py` to cover every I/O and edge-case matrix row: registration fallback, mobile navigation, Arabic direction, static references, and compiled-CSS delivery.
- Pinned Tailwind CLI and core to 4.1.0 because the initially resolved 4.3.3 package requires Node 20 while the available runtime is Node 16.16. The pinned v4 toolchain compiles successfully.

## Plan Change Log

## Review Triage Log

- Review could not start: the full route requires four review subagents to be launched together, while this session permits only three concurrent child agents. The three partial launches were interrupted before their results were handled.

## Design Notes

Use deep green as the large-field color, warm off-white for reading surfaces, and gold only for focused accents. Reuse a restrained geometric motif and consistent card/section rhythm across pages; do not let ornament compete with content or registration.

## Verification

**Commands:**
- `npm install` -- expected: declared development dependencies install successfully.
- `npm run build` -- expected: Tailwind CLI produces a minified `assets/css/styles.css` with zero browser runtime.
- `python3 -m http.server 8000` -- expected: Home, Programs, About, scripts, and styles load through static HTTP.
- `python3` static link/content audit -- expected: all local references resolve and required registration/contact targets and page landmarks are present.

**Manual checks:**
- Inspect 320px, 375px, 768px, and desktop widths for first-viewport registration, no horizontal overflow, readable long-form content, keyboard focus, mobile-menu fallback, and correct Arabic direction.

**Run results (2026-09-26):**
- `npm install`: passed; 27 packages audited, 0 vulnerabilities.
- `npm run build`: passed with Tailwind CSS v4.1.0; minified `assets/css/styles.css` generated.
- `python3 -m unittest discover -s tests -v`: 5 tests passed, covering all four edge-case matrix scenarios.
- Static content audit: passed for landmarks, registration targets, RTL Arabic, local references, and absence of Tailwind browser runtime.

## Auto Run Result

- **Status:** blocked
- **Blocking condition:** no subagents — the mandatory four-lens thorough review cannot be launched simultaneously within the platform's three-child concurrency limit.
- **Implementation completed:** Home, Programs, and About pages; shared accessible navigation; compiled Tailwind CSS; static matrix test coverage.
- **Verification completed:** Tailwind production build passed; all five static-site tests passed; static content audit passed.
- **Review state:** no review results were consumed or triaged because the complete lens set could not be launched.
