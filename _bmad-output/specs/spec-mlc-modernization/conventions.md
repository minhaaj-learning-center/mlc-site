# Implementation and Design Conventions

## Site structure

- Produce three independently addressable pages: Home, Programs, and About.
- Use a consistent header, mobile navigation, footer, registration action, and contact presentation across pages.
- Use semantic HTML landmarks and a logical heading hierarchy.
- Keep JavaScript progressive and limited to behavior that HTML and CSS cannot provide cleanly, such as mobile-navigation state.
- Compile Tailwind classes into a static production stylesheet; do not load Tailwind's browser runtime.

## Delivery

- Keep source and deployment configuration in GitHub.
- Use relative, static-safe asset and page references compatible with CDN delivery and the GoDaddy-managed public domain.
- Keep deployment free of server-side runtime requirements.

## Mobile-first behavior

- Start layouts at narrow phone widths and add enhancements with min-width breakpoints.
- Keep primary actions comfortably tappable and visible without horizontal scrolling.
- Ensure navigation works with touch and keyboard input and exposes its expanded state to assistive technology.
- Avoid dense walls of text by using clear sections, short measures, and progressive disclosure only when content remains accessible without JavaScript.

## Visual direction

- Use a deep, natural green inspired by the Kubba Khadra as the dominant institutional color.
- Use gold sparingly for emphasis, borders, small ornamental details, and primary-action accents; maintain readable contrast.
- Favor generous whitespace, restrained geometry, refined typography, and subtle Islamic visual references over ornate decoration.
- Build the hero entirely with HTML and CSS: institution name, concise value proposition, weekend-school context, primary registration action, and optional lightweight geometric ornament.
- Do not use images containing essential text.
- Use the supplied local photography as supporting visual content: optimize it for web delivery, provide descriptive alternative text, and keep it subordinate to the page's authored copy and actions.

## Quality floor

- Provide visible focus states, descriptive link text, keyboard-operable controls, appropriate labels, and sufficient text/background contrast.
- Avoid layout shift from fonts or decorative assets and keep the first mobile view lightweight.
- Confirm current versions of Chrome, Safari, Firefox, and Edge render all content and actions correctly at phone and desktop widths.
- Treat Arabic as bidirectional content with appropriate language and direction attributes rather than styling it as an image.
