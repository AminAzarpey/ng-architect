# Breadcrumb (`p-breadcrumb`)

Breadcrumb provides contextual information about page hierarchy.

**Import:**

```ts
import { BreadcrumbModule } from "primeng/breadcrumb";
import { MenuItem } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { BreadcrumbModule } from "primeng/breadcrumb";
import { MenuItem } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-breadcrumb [model]="items" [home]="home" />
    </div>
  `,
  standalone: true,
  imports: [BreadcrumbModule],
})
export class BreadcrumbBasicDemo implements OnInit {
  items: MenuItem[] | undefined;
  home: MenuItem | undefined;

  ngOnInit() {
    this.items = [
      { label: "Electronics" },
      { label: "Computer" },
      { label: "Accessories" },
      { label: "Keyboard" },
      { label: "Wireless" },
    ];
    this.home = { icon: "pi pi-home" };
  }
}
```

## Inputs

| Name          | Type                     | Default | Description                                                   |
| ------------- | ------------------------ | ------- | ------------------------------------------------------------- |
| model         | MenuItem[]               | -       | An array of menuitems.                                        |
| style         | { [klass: string]: any } | -       | Inline style of the component.                                |
| styleClass    | string                   | -       | Style class of the component.                                 |
| home          | MenuItem                 | -       | MenuItem configuration for the home icon.                     |
| homeAriaLabel | string                   | -       | Defines a string that labels the home icon for accessibility. |

## Outputs

| Name        | Parameters                      | Description                     |
| ----------- | ------------------------------- | ------------------------------- |
| onItemClick | event: BreadcrumbItemClickEvent | Fired when an item is selected. |

## Templates

| Name      | Type                                       | Description                |
| --------- | ------------------------------------------ | -------------------------- |
| item      | TemplateRef<BreadcrumbItemTemplateContext> | Custom item template.      |
| separator | TemplateRef<void>                          | Custom separator template. |

**Full API & more examples:** https://primeng.org/breadcrumb
