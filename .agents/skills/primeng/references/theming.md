# Theming (Styled Mode & Design Tokens)

PrimeNG is design-agnostic: styling is decoupled into **themes** made of a **base** (style rules with CSS-variable placeholders) and a **preset** (design tokens mapping to those variables). Configure it via `providePrimeNG({ theme })`. Tokens, not CSS overrides, are the supported way to customize.

> This is the v18+ model (`@primeuix/themes`). It replaced the old per-theme CSS files. Verify against the installed version.

## Design token tiers

1. **Primitive** — context-free palette, e.g. `blue.500`, `{zinc.100}`.
2. **Semantic** — intent-based, e.g. `primary.color`, `surface.*`, focus ring. Map to primitives. The special `colorScheme` group defines light/dark values.
3. **Component** — per-component, e.g. `inputtext.background`, `button.color`. Map to semantic tokens.

**Best practice:** customize via primitive + semantic tokens in a custom preset. Use component tokens only for targeted tweaks. Avoid overriding with CSS classes — it's the last resort.

## Built-in presets

`Aura` (PrimeTek), `Material` (Material Design v2), `Lara` (Bootstrap-like), `Nora` (enterprise). Import from `@primeuix/themes/<name>`:

```ts
import Aura from "@primeuix/themes/aura";
providePrimeNG({ theme: { preset: Aura } });
```

## Customize a preset — `definePreset`

```ts
import { definePreset } from "@primeuix/themes";
import Aura from "@primeuix/themes/aura";

const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: "{indigo.50}",
      100: "{indigo.100}",
      /* … */ 500: "{indigo.500}",
      /* … */ 950: "{indigo.950}",
    },
    colorScheme: {
      light: { surface: { 0: "#ffffff", 50: "{zinc.50}" /* … */ } },
      dark: { surface: { 0: "#ffffff", 50: "{zinc.800}" /* … */ } },
    },
  },
});

providePrimeNG({ theme: { preset: MyPreset } });
```

**Common pitfall:** if the original preset defines a token under `colorScheme`, you must override it under `colorScheme` too — a direct value will be ignored. Mirror the original structure.

## `options` (CSS generation)

```ts
theme: {
  preset: Aura,
  options: {
    prefix: "p",                 // CSS var prefix → var(--p-primary-color)
    darkModeSelector: "system",  // see Dark mode below
    cssLayer: false,             // wrap PrimeNG styles in a `primeng` cascade layer
  },
}
```

## Dark mode

Default `darkModeSelector: "system"` follows `prefers-color-scheme`. For a manual toggle, set a class selector and toggle that class on `<html>`:

```ts
providePrimeNG({
  theme: { preset: Aura, options: { darkModeSelector: ".app-dark" } },
});
```

```ts
toggleDarkMode() {
  document.documentElement.classList.toggle("app-dark");
}
```

Use `false` (or `"none"`) to disable dark mode entirely, or apply the class permanently for always-dark.

## Runtime theme APIs (from `@primeuix/themes`)

- `updatePreset(tokens)` — merge tokens into the current preset.
- `updatePrimaryPalette(palette)` / `updateSurfacePalette(palette)` — shorthand palette swaps.
- `usePreset(preset)` — replace the preset entirely at runtime.
- `$dt("primary.color")` — read a token's path/value programmatically.
- `palette("#10b981")` — generate 50–950 shades from a color.

## Scoped tokens (`dt`)

Override tokens for one component instance without `::ng-deep`:

```html
<p-toggleswitch [dt]="{ handle: { background: '{amber.500}' } }" />
```

## CSS layers & resets

Enabling `cssLayer: true` wraps PrimeNG styles in a `primeng` cascade layer so your app CSS (and Tailwind utilities) can override them predictably. If a global reset (Bootstrap reboot, Tailwind preflight) interferes with components, put it in a layer and order `@layer reset, primeng;`. See [styling-integration.md](styling-integration.md) for the Tailwind layer setup.

## Scale

Components use `rem`; adjust the root `font-size` to scale the whole UI globally.
