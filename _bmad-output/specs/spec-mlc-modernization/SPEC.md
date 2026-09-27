---
id: SPEC-mlc-modernization
companions:
  - content-inventory.md
  - conventions.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the complete, preservation-validated contract for what to build, test, and validate.

# MLC Website Modernization

## Why

Minhaaj Learning Center needs a clear, credible mobile presence that makes registration immediate and presents its mission and programs without the visual and navigational weight of the current site. Mobile visitors, prospective students, and families should quickly understand what MLC teaches, why it exists, and how to enroll.

## Capabilities

- **CAP-1**
  - **intent:** Visitors can understand MLC's offer and begin registration immediately from the homepage hero.
  - **success:** At a mobile viewport, the initial screen contains a prominent working registration action and an HTML/CSS presentation rather than a flyer image.
- **CAP-2**
  - **intent:** Visitors can learn MLC's mission, curriculum breadth, and commitment to its community from the homepage.
  - **success:** The homepage represents every load-bearing item in the Home inventory, including the mission and contact information, in readable sections.
- **CAP-3**
  - **intent:** Visitors can explore Weekend School Sessions, Knowledge Retreats, and the course offering from a dedicated Programs page.
  - **success:** All three program groups and every course topic in the Programs inventory are discoverable without requiring separate course-detail pages.
- **CAP-4**
  - **intent:** Visitors can understand MLC's history, religious purpose, educational approach, and intended audience from a dedicated About page.
  - **success:** The About page preserves the source's meaning, Arabic quotation and translation, teaching areas, and commitment to face-to-face community education.
- **CAP-5**
  - **intent:** Mobile visitors can move among the three pages and reach registration or MLC contact channels without friction.
  - **success:** Home, Programs, and About are reachable through usable narrow-screen navigation, and the registration, phone, email, and address actions resolve to their intended destinations.

## Constraints

- Deliver a static multi-page site using vanilla HTML, vanilla JavaScript, and Tailwind-generated CSS; ship compiled CSS with no Tailwind browser runtime and no application framework.
- Design mobile-first, then enhance layouts for wider screens without reducing mobile content or functionality.
- Use a modern, elegant, minimal visual language appropriate to an Islamic religious institution, with Kubba Khadra-inspired green as the primary color and restrained gold accents.
- Use only content derived from the current Home, Programs, and About pages; follow `content-inventory.md` for preservation scope.
- Use the confirmed current Google Form as the launch registration destination.
- Keep the project source on GitHub and make the static site suitable for connection to the GoDaddy-managed domain and CDN delivery.
- Follow `conventions.md` for structure, responsive behavior, accessibility, and visual implementation.

## Non-goals

- Rebuilding Calendar, Contact, registration, course catalog, or individual course-detail pages.
- Adding a CMS, application backend, authentication, payments, or an on-site registration form.
- Reproducing the current flyer image or using image-based text in the hero.
- Creating new religious claims, program offerings, schedules, or institutional content not present in the three source pages.

## Success signal

- On a mobile device, a prospective family can identify MLC, open registration from the first viewport, understand its mission and offerings, navigate all three pages, and contact or locate the center without encountering image-based text, horizontal scrolling, or broken actions.

## Assumptions

- Existing prose may be lightly corrected and reorganized for clarity while preserving its religious meaning and factual claims.
- The current authored wording is canonical: use “Qur'an” throughout, describe Fiqh as guided by Islam's core pillars and the conditions and integrals of worship, and describe Tafseer as helping students understand Qur'anic guidance and meanings of verses that befit Allah.
- The current address, phone number, and email remain valid until MLC provides replacements.
