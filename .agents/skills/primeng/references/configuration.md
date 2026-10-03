# Configuration

Application-wide options are set via `providePrimeNG(...)` at bootstrap, and can be changed at runtime by injecting the `PrimeNG` service (from `primeng/config`).

## `providePrimeNG` options

```ts
import { providePrimeNG } from "primeng/config";
import Aura from "@primeuix/themes/aura";

providePrimeNG({
  theme: {
    preset: Aura,
    options: { prefix: "p", darkModeSelector: "system", cssLayer: false },
  },
  ripple: true, // enable ripple animation on buttons etc. (off by default)
  inputVariant: "outlined", // or "filled"
  overlayAppendTo: "self", // or "body" — default overlay mount point
  csp: { nonce: "..." }, // nonce for dynamically generated <style> tags
  translation: { accept: "Aceptar", reject: "Rechazar" /* … */ },
});
```

`theme` is detailed in [theming.md](theming.md).

## Runtime changes — `PrimeNG` service

```ts
import { Component, inject } from "@angular/core";
import { PrimeNG } from "primeng/config";

@Component({
  /* ... */
})
export class AppComponent {
  private primeng = inject(PrimeNG);
  ngOnInit() {
    this.primeng.ripple.set(true);
    this.primeng.setTranslation({ accept: "Yes", reject: "No" });
  }
}
```

## Locale / translations

Default text (filter labels, month names, "accept"/"reject", etc.) is set via `translation` at bootstrap or `setTranslation(...)` at runtime. Ready-made locales live in the community **PrimeLocale** repo; integrate dynamic switching with `@ngx-translate/core` by piping the loaded `primeng` translation object into `setTranslation`.

## DataTable filter modes

Customize default filter match modes (used by Table filter menus):

```ts
import { FilterMatchMode } from "primeng/api";

this.primeng.filterMatchModeOptions.set({
  text: [
    FilterMatchMode.STARTS_WITH,
    FilterMatchMode.CONTAINS,
    FilterMatchMode.EQUALS,
  ],
  numeric: [
    FilterMatchMode.EQUALS,
    FilterMatchMode.LESS_THAN,
    FilterMatchMode.GREATER_THAN,
  ],
  date: [
    FilterMatchMode.DATE_IS,
    FilterMatchMode.DATE_BEFORE,
    FilterMatchMode.DATE_AFTER,
  ],
});
```

## z-index layering

Overlays are layered automatically. Override category defaults when you have fixed layout chrome:

```ts
this.primeng.zIndex = {
  modal: 1100, // dialog, drawer
  overlay: 1000, // select, popover
  menu: 1000, // overlay menus
  tooltip: 1100,
};
```

> The older `PrimeNGConfig` (from `primeng/api`) is superseded by the `PrimeNG` service in current versions — prefer `providePrimeNG` + `PrimeNG`. Verify against the installed version.
