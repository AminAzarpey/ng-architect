# Menu (`p-menu`)

Menu is a navigation / command component that supports dynamic and static positioning.

**Import:**

```ts
import { MenuModule } from "primeng/menu";
import { MenuItem } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { MenuModule } from "primeng/menu";
import { MenuItem } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-menu [model]="items" />
    </div>
  `,
  standalone: true,
  imports: [MenuModule],
})
export class MenuBasicDemo implements OnInit {
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      { label: "New", icon: "pi pi-plus" },
      { label: "Search", icon: "pi pi-search" },
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
| autoZIndex     | boolean                    | true    | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex     | number                     | 0       | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| ariaLabel      | string                     | -       | Defines a string value that labels an interactive element.                                                                                                                                                                                           |
| ariaLabelledBy | string                     | -       | Identifier of the underlying input element.                                                                                                                                                                                                          |
| id             | string                     | -       | Current id state as a string.                                                                                                                                                                                                                        |
| tabindex       | number                     | 0       | Index of the element in tabbing order.                                                                                                                                                                                                               |
| appendTo       | InputSignal<any>           | 'self'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions  | InputSignal<MotionOptions> | ...     | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name    | Parameters   | Description                                      |
| ------- | ------------ | ------------------------------------------------ |
| onShow  | value: any   | Callback to invoke when overlay menu is shown.   |
| onHide  | value: any   | Callback to invoke when overlay menu is hidden.  |
| onBlur  | event: Event | Callback to invoke when the list loses focus.    |
| onFocus | event: Event | Callback to invoke when the list receives focus. |

## Templates

| Name          | Type                                          | Description                         |
| ------------- | --------------------------------------------- | ----------------------------------- |
| start         | TemplateRef<void>                             | Defines template option for start.  |
| end           | TemplateRef<void>                             | Defines template option for end.    |
| header        | TemplateRef<void>                             | Defines template option for header. |
| item          | TemplateRef<MenuItemTemplateContext>          | Custom item template.               |
| submenuheader | TemplateRef<MenuSubmenuHeaderTemplateContext> | Custom submenu header template.     |

## Methods

| Name   | Parameters   | Return Type | Description                               |
| ------ | ------------ | ----------- | ----------------------------------------- |
| toggle | event: Event | void        | Toggles the visibility of the popup menu. |
| show   | event: any   | void        | Displays the popup menu.                  |
| hide   |              | void        | Hides the popup menu.                     |

**Full API & more examples:** https://primeng.org/menu
