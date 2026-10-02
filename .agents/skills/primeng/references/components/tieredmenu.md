# TieredMenu (`p-tieredmenu`)

TieredMenu displays submenus in nested overlays.

**Import:**

```ts
import { TieredMenuModule } from "primeng/tieredmenu";
import { MenuItem } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { TieredMenuModule } from "primeng/tieredmenu";
import { MenuItem } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-tieredmenu [model]="items" />
    </div>
  `,
  standalone: true,
  imports: [TieredMenuModule],
})
export class TieredmenuBasicDemo implements OnInit {
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      {
        label: "File",
        icon: "pi pi-file",
        items: [
          {
            label: "New",
            icon: "pi pi-plus",
            items: [
              {
                label: "Document",
                icon: "pi pi-file",
              },
              {
                label: "Image",
                icon: "pi pi-image",
              },
              {
                label: "Video",
                icon: "pi pi-video",
              },
            ],
          },
          {
            label: "Open",
            icon: "pi pi-folder-open",
          },
          {
            label: "Print",
            icon: "pi pi-print",
          },
        ],
      },
      {
        label: "Edit",
        icon: "pi pi-file-edit",
        items: [
          {
            label: "Copy",
            icon: "pi pi-copy",
          },
          {
            label: "Delete",
            icon: "pi pi-times",
          },
        ],
      },
      {
        label: "Search",
        icon: "pi pi-search",
      },
      {
        separator: true,
      },
      {
        label: "Share",
        icon: "pi pi-share-alt",
        items: [
          {
            label: "Slack",
            icon: "pi pi-slack",
          },
          {
            label: "Whatsapp",
            icon: "pi pi-whatsapp",
          },
        ],
      },
    ];
  }
}
```

## Inputs

| Name           | Type                       | Default | Description                                                                                                                                                                                                                                          |
| -------------- | -------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model          | MenuItem[]                 | -       | An array of menuitems.                                                                                                                                                                                                                               |
| popup          | boolean                    | false   | Defines if menu would displayed as a popup.                                                                                                                                                                                                          |
| style          | { [klass: string]: any }   | -       | Inline style of the component.                                                                                                                                                                                                                       |
| styleClass     | string                     | -       | Style class of the component.                                                                                                                                                                                                                        |
| breakpoint     | string                     | 960px   | The breakpoint to define the maximum width boundary.                                                                                                                                                                                                 |
| autoZIndex     | boolean                    | true    | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex     | number                     | 0       | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| autoDisplay    | boolean                    | true    | Whether to show a root submenu on mouse over.                                                                                                                                                                                                        |
| id             | string                     | -       | Current id state as a string.                                                                                                                                                                                                                        |
| ariaLabel      | string                     | -       | Defines a string value that labels an interactive element.                                                                                                                                                                                           |
| ariaLabelledBy | string                     | -       | Identifier of the underlying input element.                                                                                                                                                                                                          |
| disabled       | boolean                    | false   | When present, it specifies that the component should be disabled.                                                                                                                                                                                    |
| tabindex       | number                     | 0       | Index of the element in tabbing order.                                                                                                                                                                                                               |
| appendTo       | InputSignal<any>           | 'self'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions  | InputSignal<MotionOptions> | ...     | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name   | Parameters | Description                                     |
| ------ | ---------- | ----------------------------------------------- |
| onShow | value: any | Callback to invoke when overlay menu is shown.  |
| onHide | value: any | Callback to invoke when overlay menu is hidden. |

## Templates

| Name        | Type                                       | Description                   |
| ----------- | ------------------------------------------ | ----------------------------- |
| submenuicon | TemplateRef<void>                          | Custom submenu icon template. |
| item        | TemplateRef<TieredMenuItemTemplateContext> | Custom item template.         |

## Methods

| Name   | Parameters                   | Return Type | Description                               |
| ------ | ---------------------------- | ----------- | ----------------------------------------- |
| hide   | event: any, isFocus: boolean | void        | Hides the popup menu.                     |
| toggle | event: any                   | void        | Toggles the visibility of the popup menu. |
| show   | event: any, isFocus: any     | void        | Displays the popup menu.                  |

**Full API & more examples:** https://primeng.org/tieredmenu
