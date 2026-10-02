# Installation & Setup

PrimeNG is a standalone-component library (v17+). You import the component you use directly — there is **no root `NgModule`** to register.

## Install

```sh
npm install primeng @primeuix/themes
npm install primeicons   # optional: the default icon set
```

`@primeuix/themes` provides the theme presets (Aura, Material, Lara, Nora) and the theming utilities (`definePreset`, `$dt`, `palette`, …). See [theming.md](theming.md).

## Configure the provider

Add `providePrimeNG` (from `primeng/config`) and Angular's async animations provider in `app.config.ts`:

```ts
import { ApplicationConfig } from "@angular/core";
import { provideAnimationsAsync } from "@angular/platform-browser/animations/async";
import { providePrimeNG } from "primeng/config";
import Aura from "@primeuix/themes/aura";

export const appConfig: ApplicationConfig = {
  providers: [
    provideAnimationsAsync(),
    providePrimeNG({
      theme: { preset: Aura },
    }),
  ],
};
```

- **`provideAnimationsAsync()`** is required for components with transitions/overlays (Dialog, Toast, menus, etc.).
- For `NgModule` apps, call the same providers in `bootstrapApplication`/the root module providers.

## Import PrimeIcons CSS

In `styles.scss` (or `angular.json` styles):

```scss
@import "primeicons/primeicons.css";
```

## Use a component

Import the component class (or its `XxxModule`) into the standalone component's `imports`:

```ts
import { Component } from "@angular/core";
import { ButtonModule } from "primeng/button";

@Component({
  selector: "app-demo",
  standalone: true,
  imports: [ButtonModule],
  template: `<p-button label="Save" icon="pi pi-check" />`,
})
export class DemoComponent {}
```

Each component's import path is documented in its reference file under `references/components/`.

## Next steps

- [configuration.md](configuration.md) — global options (`ripple`, `zIndex`, locale, filter modes, CSP).
- [theming.md](theming.md) — presets, design tokens, dark mode.
- [styling-integration.md](styling-integration.md) — Tailwind, passthrough (`pt`), unstyled mode.

> Verify versions against the project's installed `primeng` (this skill targets **v21**). Setup changed significantly at v18 (the `@primeuix/themes` design-token model replaced the old CSS theme files).
