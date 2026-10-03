# Icons (PrimeIcons)

PrimeIcons is PrimeNG's default icon library (250+ icons).

## Install

```sh
npm install primeicons
```

```scss
/* styles.scss */
@import "primeicons/primeicons.css";
```

## Usage

Syntax is `pi pi-<name>` on an `<i>` or `<span>`:

```html
<i class="pi pi-check"></i>
<i
  class="pi pi-times"
  style="font-size: 2rem; color: var(--p-primary-color)"
></i>
<i class="pi pi-spinner pi-spin"></i>
```

- **Size:** controlled by `font-size`.
- **Color:** inherited from parent; set via `color`.
- **Spin:** add `pi-spin` for infinite rotation.

Most components accept an `icon` input that takes the class string, e.g. `<p-button icon="pi pi-search" />`.

## Programmatic constants

Use the `PrimeIcons` constants (from `primeng/api`) for menu items etc.:

```ts
import { PrimeIcons, MenuItem } from "primeng/api";

const items: MenuItem[] = [
  { label: "New", icon: PrimeIcons.PLUS },
  { label: "Delete", icon: PrimeIcons.TRASH },
];
```

## Custom icons

FontAwesome, Material Icons, images, or inline SVG can be used anywhere an icon class or icon template slot is accepted — see [styling-integration.md](styling-integration.md).
