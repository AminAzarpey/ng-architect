# Accessibility

PrimeNG targets **WCAG 2.1 AA** compliance. Components ship with keyboard and screen-reader support built on semantic HTML + WAI-ARIA (each component's full docs page has a "Accessibility" section documenting roles, ARIA attributes, and keyboard shortcuts).

## What PrimeNG gives you

- Native form controls under the hood (e.g. Checkbox renders a hidden native `<input>`), so focus, keyboard, and reader support work out of the box.
- ARIA roles/states/properties applied to rich widgets (datepicker, dialog, menus, etc.).
- A `p-sr-only` utility class to expose content to screen readers while hiding it visually.

## Your responsibilities

- **Label every form control.** Associate a `<label>` (or `ariaLabel`/`ariaLabelledBy` inputs that many components expose) so the purpose is announced.
- **Prefer semantic HTML** around components instead of generic `div`s.
- **Color contrast:** aim for ≥ 4.5:1 foreground/background; avoid vibrating color pairs; use desaturated colors in dark mode to reduce eye strain (tune via theme tokens — [theming.md](theming.md)).
- **Don't remove focus outlines.** Customize the focus ring through the `focus.ring.*` design tokens rather than disabling it.
- Pass any extra ARIA attributes you need through `pt` ([styling-integration.md](styling-integration.md)) when a component doesn't expose a dedicated input.

## Common component inputs

Many components accept `ariaLabel`, `ariaLabelledBy`, and `inputId` to wire up labels and describe purpose — check the component's reference/inputs table.
