# Choosing UI libraries

PrimeNG, Angular Material, and Tailwind CSS are supported together. Keep all three installed and configured. Each feature chooses its component library through its standalone component imports and templates; no global library switch is required. Tailwind supplies layout and utilities alongside either component library, or for custom native elements.

## Available configuration

| Library          | Configuration                                                                                 | How to select it                                                          |
| ---------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| PrimeNG          | Aura preset via `providePrimeNG` in `src/app/app.config.ts`; PrimeIcons CSS in `angular.json` | Import the needed PrimeNG components/modules into the consuming component |
| Angular Material | `mat.theme()` in `src/styles.scss`; CDK installed                                             | Import the needed Material modules into the consuming component           |
| Tailwind CSS     | `.postcssrc.json`, `src/tailwind.css`, and the global styles entry in `angular.json`          | Add utility classes to templates; no Angular component import needed      |

## Choosing components in code

A standalone component can use either library, or both when the screen calls for it:

```ts
import { ChangeDetectionStrategy, Component } from "@angular/core";
import { MatButtonModule } from "@angular/material/button";
import { ButtonModule } from "primeng/button";

@Component({
  selector: "app-ui-example",
  imports: [MatButtonModule, ButtonModule],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="flex flex-wrap items-center gap-4 p-4">
      <button matButton type="button">Material action</button>
      <p-button label="PrimeNG action" />
      <button type="button" class="rounded border px-4 py-2">Tailwind action</button>
    </div>
  `,
})
export class UiExample {}
```

Import only what the consuming component uses. The example demonstrates selection in code; a runtime preference does not automatically replace one library's components with another's.

## PrimeNG and Tailwind integration

`tailwindcss-primeui` 0.6.1 is installed alongside Tailwind 4. Its CSS import in `src/tailwind.css` exposes utilities such as `bg-primary`, `text-primary-contrast`, `text-muted-color`, `bg-surface-100`, and `rounded-border`, backed by PrimeNG theme tokens. Plain Tailwind utilities remain available for Material controls and native elements. The current Material root font is 14px, so rem-based spacing follows that scale (`p-2` is 0.5rem, currently 7px).

```html
<section class="rounded-border bg-surface-100 p-4">
  <p class="text-muted-color">PrimeNG theme colors with Tailwind layout.</p>
  <div class="flex flex-wrap items-center gap-4">
    <button pButton type="button" class="p-2">PrimeNG with utility spacing</button>
    <button matButton type="button" class="mt-2">Material with utility layout</button>
    <button type="button" class="rounded-border bg-primary px-4 py-2 text-primary-contrast">Native control with PrimeNG semantic colors</button>
  </div>
</section>
```

Import `ButtonModule` and `MatButtonModule` in the consuming standalone component for that example. Semantic color utilities use PrimeNG tokens; Material controls retain their Material theme tokens. A shared palette can be defined through the respective theme APIs when a feature needs visual alignment.

PrimeNG styles use the `primeng` CSS layer. The global order is `theme, base, primeng, components, utilities`, allowing utilities to override layered PrimeNG rules. Material's generated styles remain under its own theme control; use its public theme APIs for colors and typography instead of relying on utility specificity against internal selectors.

## Shared dark mode

The default is light mode. PrimeNG's `darkModeSelector`, Tailwind's `dark` variant, and Material's `color-scheme` all follow `.app-dark` on the document root. Toggle the class in presentation code to switch the three systems together:

```ts
document.documentElement.classList.toggle("app-dark", true); // dark
// Use false to return to light mode.
```

Use Angular's injected `DOCUMENT` when implementing a theme service. This configuration provides the styling contract; an application theme toggle and preference persistence can be added by the consuming feature.

See the [official integration package](https://github.com/primefaces/tailwindcss-primeui) and [PrimeNG 21 Tailwind guide](https://v21.primeng.org/tailwind).

## Design and domain boundaries

Keep library imports in feature presentation components and reusable UI wrappers. Domain models and application use cases remain independent of Material, PrimeNG, and Tailwind. Choose components based on interaction needs and keep typography, spacing, colors, density, and focus behavior consistent across the feature.

Retain both the Material Sass theme and PrimeNG's provider. Customize Material through its Sass/theme APIs and PrimeNG through design tokens. Prefer Tailwind for layout and spacing; avoid broad selectors or styling internal component DOM that could affect the other library. Tailwind's base reset is global, so verify the appearance of real controls from both libraries when changing global styles.

When adding mixed-library screens, check keyboard navigation, focus restoration, validation states, dark mode, overlay stacking, responsive layout, and production bundle budgets. Library availability does not establish compatibility for every component combination. PrimeNG is pinned to the MIT-licensed v21 line and needs no activation key; see the [license choice](PRIMEUI-LICENSE.md).

## References

- [PrimeNG setup and per-component imports](https://v21.primeng.org/installation)
- [Angular Material buttons](https://material.angular.dev/components/button/overview)
- [Angular Tailwind integration](https://angular.dev/guide/tailwind)
