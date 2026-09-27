---
title: 'Address website review findings'
type: 'bugfix'
ticket: ''
created: '2026-09-26'
status: 'built'
route: 'full'
route_source: 'auto'
baseline_revision: 'NO_VCS'
blocked_reason: ''
review: 'thorough'
review_source: 'auto'
lenses_ran:
  - blind-hunter
  - edge-case-hunter
  - verification-gap
  - intent-alignment
review_loop_iteration: 1
followup_review_recommended: true
context:
  - '{project-root}/_bmad-output/specs/spec-mlc-modernization/SPEC.md'
  - '{project-root}/_bmad-output/specs/spec-mlc-modernization/content-inventory.md'
  - '{project-root}/_bmad-output/specs/spec-mlc-modernization/conventions.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** The completed static site has accessibility, maintainability, and verification gaps identified by review: inaccurate menu labeling, insufficient contrast, motion without a reduced-motion path, unused icon metadata, stale-prone shared content, weak tests, and no standard test command.

**Approach:** Correct the runtime and presentation defects across all three pages, strengthen the existing lightweight Python verification suite, and expose one reliable package-level test command without adding a framework or changing approved institutional content.

## Boundaries & Constraints

**Always:** Preserve the three-page static architecture, approved registration/contact destinations, semantic progressive navigation, supplied religious wording, vanilla JavaScript, Tailwind-generated CSS, and usable no-JavaScript fallback. Apply shared changes consistently on Home, Programs, and About.

**Never:** Add a client framework, server runtime, templating system, browser-test dependency, or unsupported religious attribution. Do not alter schedules, institutional claims, contact information, or registration behavior.

**Decision:** Defer religious-source citations until a content owner supplies approved exact sources; preserve the current wording in this change.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Mobile menu state | Details menu toggles open or closed | `aria-expanded` and its action label both match the state | Native details navigation remains usable without JavaScript |
| Reduced motion | Visitor requests reduced motion | Smooth scrolling and nonessential transitions are disabled | Static styling and controls remain intact |
| Shared page chrome | Any of the three pages loads | Favicon, contact actions, current year hook, and new-tab disclosure are consistent | Static fallback year and visible link text remain usable |
| Verification | A local asset, mobile link, CTA, CSS build, or contact target regresses | The normal test command fails on the affected contract | Failure names the page or missing contract |

</frozen-after-approval>

## Code Map

- `assets/js/site.js` -- synchronize menu expanded state and accessible action label; update current-year hooks while preserving the static fallback.
- `src/input.css` -- darken functional gold text and add reduced-motion overrides; regenerate `assets/css/styles.css` through the existing build command only.
- `index.html`, `programs.html`, `about.html` -- add favicon metadata, shared accessibility fixes, contact/year parity, and maintainable formatting without changing approved copy.
- `assets/icon.png` -- existing 512px icon to reuse as the favicon; do not replace or remove it.
- `tests/test_static_site.py` -- extend structural parsing and assertions for linked assets, scoped mobile navigation, hero registration, contact destinations, shared chrome, state labels, and compiled CSS content.
- `tests/test_site_js.mjs` -- execute the dependency-free site script against a minimal DOM harness to verify menu state labels, responsive cleanup compatibility, and deterministic current-year updates.
- `package.json` -- add the canonical test command, rebuilding generated CSS before Python verification.

## Tasks & Acceptance

**Execution:**
- [x] `assets/js/site.js` -- synchronize expanded state, open/close labeling, and current-year hooks while retaining native fallback behavior.
- [x] `src/input.css`, `assets/css/styles.css` -- meet normal-text contrast needs, honor reduced motion, and regenerate the deployable stylesheet.
- [x] `index.html`, `programs.html`, `about.html` -- apply favicon, external-tab disclosure, footer contrast/year, and shared-markup fixes consistently; reformat dense markup for reviewability.
- [x] `tests/test_static_site.py`, `package.json` -- make the normal test path rebuild CSS and verify the browser-facing contracts that the prior suite missed.
- [x] `tests/test_site_js.mjs`, `tests/test_static_site.py`, `package.json` -- execute changed JavaScript behavior, isolate the hero CTA structurally, protect required inventory content, and verify CSS rules are attached to their intended selectors/media query.

**Acceptance Criteria:**
- Given any page and menu state, when assistive technology reads the mobile trigger, then its expanded state and action label agree.
- Given the site styles, when contrast and reduced-motion behavior are inspected, then small functional text meets the accessibility floor and requested motion reduction is honored.
- Given any page, when shared chrome is inspected, then the favicon, external-tab disclosure, current-year behavior, and canonical contact links are consistent.
- Given `npm test`, when generated CSS or a required page contract is broken, then verification fails with an actionable assertion.
- Given the site script runs against controlled menu, media-query, and date states, when the normal test command executes, then open/close labels, legacy media-query fallback, and current-year output are behaviorally verified without a browser-test dependency.

## Implementation Notes

- Updated menu state announcements and current-year enhancement in `assets/js/site.js`, retaining native `<details>` and static-year fallbacks.
- Applied contrast and reduced-motion fixes in source CSS and regenerated the committed production stylesheet.
- Added favicon metadata, new-tab disclosures, consistent footer treatment, and readable formatting across all three pages without changing approved copy.
- Expanded the Python contract tests and added `npm test` so verification rebuilds CSS before running all six tests.
- `npm test` and `git diff --check` passed. npm could not write its user-level debug log inside the sandbox, but this did not affect build or tests.
- Added a dependency-free Node VM harness for menu, responsive-cleanup, and current-year behavior; strengthened structural HTML, inventory, registration, disclosure, and selector-aware CSS checks. The final suite runs 3 JavaScript checks and 8 Python tests.

## Plan Change Log

- 2026-09-26 — Thorough review found that source-string assertions did not execute the changed menu/year behavior and that structural/CSS tests could pass while their user-facing contracts were broken. Amend verification to include a dependency-free Node DOM harness, correct hero scoping, content-inventory guards, and selector-aware CSS checks. Avoid the known-bad state where expected strings remain in unreachable or mis-scoped code. KEEP the implemented accessible action labels, native `<details>` fallback, canonical destinations, favicon metadata, reduced-motion rules, contrast adjustment, and current-year fallback.

## Review Triage Log

### 2026-09-26 — Review pass
- verdicts: 23 findings — high 0, medium 8, low 4, false 8, maybe-false 3
- findings:
  - `[medium]` `[defer]` Registration-open wording is time-sensitive — it predates this change and needs content-owner confirmation.
  - `[false]` `[reject]` Favicon asset is absent — `assets/icon.png` exists and the linked-asset test resolves it.
  - `[medium]` `[defer]` Community-wide benefit is not stated distinctly — the omission predates this change and remains a content follow-up.
  - `[false]` `[reject]` Islamic Manners citations were removed — the wording is unchanged from the baseline and exact religious-source citations are explicitly deferred by intent.
  - `[low]` `[defer]` The course-card Arabic title omits its audience — this pre-existing content compression can reduce discoverability.
  - `[low]` `[defer]` The Qur'aan course title is abbreviated — this predates the review-fix change and the description preserves recitation/memorization.
  - `[false]` `[reject]` The About hadith needs a new citation — exact religious-source citations are explicitly excluded until approved by a content owner.
  - `[false]` `[reject]` Religious citations must be standardized now — the intent explicitly defers that content decision.
  - `[medium]` `[bad_plan]` Hero CTA verification is not scoped to the hero — splitting before the first closing section includes the header link; the plan now requires structural isolation.
  - `[medium]` `[bad_plan]` Load-bearing inventory content is largely unprotected — required curriculum and institutional copy can disappear while tests pass; the plan now requires inventory guards.
  - `[medium]` `[defer]` `MediaQueryList.addEventListener` lacks a legacy fallback — the call predates this change, but a compatibility follow-up is warranted.
  - `[maybe-false]` `[reject]` Mobile-nav parser depth may mishandle void or implicit elements — current mobile nav markup is explicitly closed and contains no reachable void-element trigger; a hypothetical future shape would only be low impact.
  - `[medium]` `[bad_plan]` Menu state behavior is not executed — source-string checks survive removal or breakage of the toggle listener; the plan now requires a dependency-free DOM execution test.
  - `[medium]` `[bad_plan]` Current-year behavior is not executed — selector/computation strings can remain while assignment is broken; the plan now requires controlled-date execution.
  - `[false]` `[reject]` Knowledge Retreats is duplicated in one heading — the live HTML contains the phrase once; the diff shows old and new representations, not duplicate DOM text.
  - `[medium]` `[bad_plan]` Runtime menu accessibility is only approximated by source inspection — same root cause as the unexecuted menu finding; add behavioral verification.
  - `[maybe-false]` `[bad_plan]` Contrast verification checks only a color token — selector-aware checks and the existing visual combination are needed to settle whether regressions remain detectable.
  - `[maybe-false]` `[bad_plan]` Reduced-motion verification checks only media-query text — selector-aware checks are needed to prove transitions and smooth scrolling are actually disabled.
  - `[false]` `[reject]` Shared chrome must be deduplicated — the intent preserves hand-authored static pages and accepts verification-driven consistency without a templating system.
  - `[low]` `[reject]` Registration/contact tests do not execute navigation — exact static anchors are the outermost practical contract for this static-site architecture.
  - `[low]` `[bad_plan]` Approved religious and institutional content is not regression-locked — same root cause as the missing inventory matrix; add focused content assertions.
  - `[false]` `[reject]` No-JavaScript fallback requires browser execution — preserved native `<details>/<summary>` structure directly supplies the fallback under the no-browser-dependency constraint.
  - `[false]` `[reject]` The standard test command diverges from intent — `npm test` directly provides the requested package interface; its internal coverage gaps are logged separately.

### 2026-09-26 — Review pass
- verdicts: 25 findings — high 0, medium 14, low 4, false 6, maybe-false 1
- findings:
  - `[medium]` `[patch]` Programs desktop registration lacks a new-tab disclosure — add the same per-link accessible text used on Home.
  - `[medium]` `[patch]` Programs mobile registration lacks a new-tab disclosure — add per-link accessible text.
  - `[medium]` `[patch]` Programs weekend-school registration lacks a new-tab disclosure — add per-link accessible text.
  - `[medium]` `[patch]` Programs closing registration CTA lacks a new-tab disclosure — add per-link accessible text.
  - `[medium]` `[patch]` About desktop registration lacks a new-tab disclosure — add per-link accessible text.
  - `[medium]` `[patch]` About mobile registration lacks a new-tab disclosure — add per-link accessible text.
  - `[medium]` `[patch]` About closing registration CTA lacks a new-tab disclosure — add per-link accessible text.
  - `[low]` `[patch]` Programs mobile summary lacks initial `aria-expanded="false"` — align its no-JavaScript state with Home.
  - `[low]` `[patch]` About mobile summary lacks initial `aria-expanded="false"` — align its no-JavaScript state with Home.
  - `[false]` `[reject]` Breakpoint cleanup moves focus to a hidden trigger — `closeMenu()` does not focus; only the separate Escape handler does.
  - `[medium]` `[patch]` Disclosure verification is page-wide rather than per link — assert each `_blank` anchor contains its own disclosure.
  - `[false]` `[reject]` The `2026` fallback is already stale — 2026 is the current year and the explicit no-JavaScript fallback required by the plan.
  - `[medium]` `[patch]` Undisclosed registration links pass verification — same root cause as the per-link disclosure defect; fix markup and assertion.
  - `[medium]` `[patch]` One disclosed link masks other undisclosed links — strengthen the assertion per anchor.
  - `[low]` `[patch]` Exact `rel` string comparison rejects valid token order/additions — compare required tokens as a set.
  - `[medium]` `[patch]` Claimed cross-page disclosure consistency is false — add missing Programs/About disclosures.
  - `[medium]` `[patch]` Broken disclosure contracts can leave `npm test` green — per-link assertions close the gap.
  - `[medium]` `[patch]` Cross-page initial menu state and registration disclosures diverge — align equivalent controls on all pages.
  - `[maybe-false]` `[reject]` Contrast is not computed for every rendered combination — current token/footer changes improve the cited surfaces; full rendered auditing would violate the no-browser-dependency boundary and no failing combination was demonstrated.
  - `[low]` `[patch]` Home footer descriptive opacity differs from Programs/About — align it to the reviewed `/70` shared value.
  - `[false]` `[reject]` Reduced motion must be browser-executed — selector-aware compiled CSS assertions verify the intended media rules under the explicit lightweight/no-browser constraint.
  - `[false]` `[reject]` Shared content must be source-deduplicated — verification-driven synchronization is the compatible reading of the static/no-template constraints.
  - `[medium]` `[patch]` Registration destinations are not asserted for every registration-labelled link — add a structural assertion that each such action uses the canonical URL.
  - `[false]` `[reject]` Exact religious wording is wholly unprotected — focused inventory assertions protect the supplied load-bearing phrases, while source citations remain intentionally deferred.
  - `[false]` `[reject]` Mock-DOM JavaScript verification is misaligned — the dependency-free harness executes the changed behavior and is the intended compromise under the no-browser-test constraint.

- Thorough review blocked before findings were consumed: the workflow requires four review subagents to launch simultaneously, but this platform permits only three concurrent child agents. The partial launch was interrupted and produced no triaged findings.

## Auto Run Result

- **Status:** built.
- **Summary:** implemented the accessibility, shared-chrome, favicon, reduced-motion, contrast, current-year, maintainability, and verification repairs across the three-page static site.
- **Files changed:** `index.html`, `programs.html`, and `about.html` now share consistent menu state, favicon, registration disclosures, footer contacts, and year hooks; `assets/js/site.js` synchronizes menu labels and years with legacy media-query support; `src/input.css` and generated `assets/css/styles.css` contain contrast and reduced-motion fixes; `tests/test_site_js.mjs` executes JavaScript behavior; `tests/test_static_site.py` verifies structural, content, link, and CSS contracts; `package.json` exposes the canonical test command.
- **Review findings:** the first pass drove a plan repair for behavioral JavaScript, hero scoping, inventory, and selector-aware CSS verification. The second pass applied medium patches for cross-page disclosures and canonical registration coverage, plus low patches for initial expanded state, safe `rel` token handling, and footer consistency. Pre-existing content questions and explicitly deferred religious citations were rejected or left outside this change as recorded in the triage log.
- **Follow-up review recommendation:** true — this pass patched at least two medium entries, specifically cross-page new-tab disclosure consistency and complete canonical-registration verification. Patched entry counts: high 0, medium 2, low 3.
- **Verification:** `npm test` rebuilt production CSS and passed 3 JavaScript behavior checks plus 8 Python tests; `git diff --check` passed. Matrix coverage includes menu state, reduced motion, shared chrome, and regression failure contracts.
- **Residual risks:** exact religious-source citations still require content-owner approval. The static fallback year remains `2026` for no-JavaScript users and should be refreshed in a future calendar-year maintenance pass. npm could not create its user-level debug log inside the sandbox, but this did not affect the build or tests.

## Verification

**Commands:**
- `npm test` -- expected: production CSS rebuild succeeds and all Python static-site tests pass.
- `git diff --check` -- expected: no whitespace errors in the change.

**Manual checks:**
- Inspect all three formatted pages for unchanged approved copy and consistent shared header/footer content.
