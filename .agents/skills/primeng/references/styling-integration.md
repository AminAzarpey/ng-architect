# Styling Integration — Tailwind, Pass Through, Unstyled, Custom Icons

How to customize PrimeNG beyond the component API and theme tokens. For design tokens/presets see [theming.md](theming.md).

## Pass Through (`pt`)

Every component exposes a `pt` property to apply arbitrary attributes/classes/listeners directly to its internal DOM elements (keyed by section name). This is the escape hatch when the component API lacks an option — "Your Components, Not Ours."

```html
<p-panel
  header="Header"
  [pt]="{
    root: { class: 'border-2' },
    header: { class: 'bg-primary', 'data-test': 'panel-head', onclick: onHeaderClick }
  }"
/>
```

- A **string** (or function returning a string) value is treated as a `class`.
- Each component's reference lists its section names under "Pass Through Options" on the full docs page (e.g. `root`, `header`, `content`). Sections that are themselves PrimeNG components are prefixed `pc` (e.g. `pcBadge`).
- **Lifecycle hooks** can be registered via the `hooks` PT key (`onInit`, `onDestroy`, …).

### Global `pt`

```ts
providePrimeNG({
  pt: {
    panel: { header: "bg-primary" },
    autocomplete: { root: "w-64" },
  },
});
```

Component-level `pt` overrides global by default. Control merging with `ptOptions`:

```html
<p-panel
  [pt]="{ ... }"
  [ptOptions]="{ mergeSections: true, mergeProps: false }"
/>
```

`mergeSections` (default `true`) adds the global sections; `mergeProps` (default `false`) replaces vs. merges individual props.

## Unstyled mode

Disable PrimeNG's design-token CSS entirely and bring your own styling (recommended: Tailwind + `pt`). Keeps behavior + accessibility, drops the look.

```ts
providePrimeNG({
  unstyled: true,
  pt: {
    button: {
      root: "bg-teal-500 hover:bg-teal-700 py-2 px-4 rounded-full border-0 flex gap-2",
      label: "text-white font-bold",
      icon: "text-white",
    },
  },
});
```

Or per-component: `<p-button unstyled [pt]="...">`. PrimeTek's **Volt UI** (Tailwind v4 over unstyled components, code-ownership model) is the reference for fully unstyled theming.

## Tailwind CSS

The core of PrimeNG does not depend on Tailwind, but the official **`tailwindcss-primeui`** plugin integrates them (works in styled and unstyled modes). It exposes PrimeNG semantic colors as utilities (`bg-primary`, `text-surface-500`, `text-muted-color`, `rounded-border`) plus variants for `styleclass`/`animateonscroll`.

**Tailwind v4** — in your CSS entry:

```css
@import "tailwindcss";
@import "tailwindcss-primeui";
```

**Tailwind v3** — add the plugin in `tailwind.config.js`:

```js
plugins: [require("tailwindcss-primeui")];
```

### Overriding components with Tailwind (specificity)

Tailwind utilities may not beat component CSS specificity. Preferred fix: enable `cssLayer: true` ([theming.md](theming.md)) and order layers so `primeng` comes before Tailwind's `utilities`:

```css
/* Tailwind v4 */
@layer theme, base, primeng, utilities;
```

Last resort: the `!` important prefix (e.g. `!bg-red-500`).

### Dark mode alignment

If you use a manual `darkModeSelector` (e.g. `.app-dark`), align Tailwind's `dark` variant to the same selector so utilities and components switch together.

## Icons

- **PrimeIcons** (default): `pi pi-<name>` on an `<i>`/`<span>`, e.g. `<i class="pi pi-check"></i>`. Size via `font-size`, spin with `pi-spin`. Reference icons programmatically via `PrimeIcons.CHECK` (from `primeng/api`). See [icons.md](icons.md).
- **Custom icons**: any FontAwesome/Material/image/inline-SVG can be used wherever an icon template or `icon` slot is accepted — pass your own markup via content projection or the relevant `*icon` template.
