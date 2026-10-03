# Menubar (`p-menubar`)

Menubar is a horizontal menu component.

**Import:**

```ts
import { MenubarModule } from "primeng/menubar";
import { MenuItem } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { MenubarModule } from "primeng/menubar";
import { MenuItem } from "primeng/api";

@Component({
  template: `
    <div class="card">
      <p-menubar [model]="items" />
    </div>
  `,
  standalone: true,
  imports: [MenubarModule],
})
export class MenubarBasicDemo implements OnInit {
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      {
        label: "Home",
        icon: "pi pi-home",
      },
      {
        label: "Features",
        icon: "pi pi-star",
      },
      {
        label: "Projects",
        icon: "pi pi-search",
        items: [
          {
            label: "Components",
            icon: "pi pi-bolt",
          },
          {
            label: "Blocks",
            icon: "pi pi-server",
          },
          {
            label: "UI Kit",
            icon: "pi pi-pencil",
          },
          {
            label: "Templates",
            icon: "pi pi-palette",
            items: [
              {
                label: "Apollo",
                icon: "pi pi-palette",
              },
              {
                label: "Ultima",
                icon: "pi pi-palette",
              },
            ],
          },
        ],
      },
      {
        label: "Contact",
        icon: "pi pi-envelope",
      },
    ];
  }
}
```

## Inputs

| Name           | Type       | Default | Description                                                       |
| -------------- | ---------- | ------- | ----------------------------------------------------------------- |
| model          | MenuItem[] | -       | An array of menuitems.                                            |
| autoZIndex     | boolean    | true    | Whether to automatically manage layering.                         |
| baseZIndex     | number     | 0       | Base zIndex value to use in layering.                             |
| autoDisplay    | boolean    | true    | Whether to show a root submenu on mouse over.                     |
| autoHide       | boolean    | false   | Whether to hide a root submenu when mouse leaves.                 |
| breakpoint     | string     | 960px   | The breakpoint to define the maximum width boundary.              |
| autoHideDelay  | number     | 100     | Delay to hide the root submenu in milliseconds when mouse leaves. |
| id             | string     | -       | Current id state as a string.                                     |
| ariaLabel      | string     | -       | Defines a string value that labels an interactive element.        |
| ariaLabelledBy | string     | -       | Identifier of the underlying input element.                       |

## Outputs

| Name    | Parameters        | Description                                  |
| ------- | ----------------- | -------------------------------------------- |
| onFocus | event: FocusEvent | Callback to execute when button is focused.  |
| onBlur  | event: FocusEvent | Callback to execute when button loses focus. |

## Templates

| Name        | Type                                    | Description                               |
| ----------- | --------------------------------------- | ----------------------------------------- |
| start       | TemplateRef<void>                       | Defines template option for start.        |
| end         | TemplateRef<void>                       | Defines template option for end.          |
| item        | TemplateRef<MenubarItemTemplateContext> | Custom item template.                     |
| menuicon    | TemplateRef<void>                       | Defines template option for menu icon.    |
| submenuicon | TemplateRef<void>                       | Defines template option for submenu icon. |

**Full API & more examples:** https://primeng.org/menubar
