# ContextMenu (`p-contextmenu`)

ContextMenu displays an overlay menu on right click of its target.

**Import:**

```ts
import { ContextMenu, ContextMenuModule } from "primeng/contextmenu";
import { MenuItem } from "primeng/api";
import { ContextMenu } from "primeng/contextmenu";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { ContextMenu, ContextMenuModule } from "primeng/contextmenu";
import { MenuItem } from "primeng/api";
import { ContextMenu } from "primeng/contextmenu";

@Component({
  template: `
    <div class="card flex justify-center">
      <img
        #img
        src="https://primefaces.org/cdn/primeng/images/demo/nature/nature2.jpg"
        alt="Logo"
        aria-haspopup="true"
        class="w-full md:w-[30rem] rounded shadow-lg"
      />
      <p-contextmenu [target]="img" [model]="items" />
    </div>
  `,
  standalone: true,
  imports: [ContextMenuModule],
})
export class ContextmenuBasicDemo implements OnInit {
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      { label: "Copy", icon: "pi pi-copy" },
      { label: "Rename", icon: "pi pi-file-edit" },
    ];
  }
}
```

## Inputs

| Name           | Type                       | Default     | Description                                                                                                                                                                                                                                          |
| -------------- | -------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model          | MenuItem[]                 | -           | An array of menuitems.                                                                                                                                                                                                                               |
| triggerEvent   | string                     | contextmenu | Event for which the menu must be displayed.                                                                                                                                                                                                          |
| target         | string \| HTMLElement      | -           | Local template variable name of the element to attach the context menu.                                                                                                                                                                              |
| global         | boolean                    | false       | Attaches the menu to document instead of a particular item.                                                                                                                                                                                          |
| style          | { [klass: string]: any }   | -           | Inline style of the component.                                                                                                                                                                                                                       |
| styleClass     | string                     | -           | Style class of the component.                                                                                                                                                                                                                        |
| autoZIndex     | boolean                    | true        | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex     | number                     | 0           | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| id             | string                     | -           | Current id state as a string.                                                                                                                                                                                                                        |
| breakpoint     | string                     | 960px       | The breakpoint to define the maximum width boundary.                                                                                                                                                                                                 |
| ariaLabel      | string                     | -           | Defines a string value that labels an interactive element.                                                                                                                                                                                           |
| ariaLabelledBy | string                     | -           | Identifier of the underlying input element.                                                                                                                                                                                                          |
| pressDelay     | number                     | 500         | Press delay in touch devices as miliseconds.                                                                                                                                                                                                         |
| appendTo       | InputSignal<any>           | 'self'      | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions  | InputSignal<MotionOptions> | ...         | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name   | Parameters  | Description                                     |
| ------ | ----------- | ----------------------------------------------- |
| onShow | value: null | Callback to invoke when overlay menu is shown.  |
| onHide | value: null | Callback to invoke when overlay menu is hidden. |

## Templates

| Name        | Type                                               | Description                   |
| ----------- | -------------------------------------------------- | ----------------------------- |
| item        | TemplateRef<ContextMenuItemTemplateContext>        | Custom item template.         |
| submenuicon | TemplateRef<ContextMenuSubmenuIconTemplateContext> | Custom submenu icon template. |

**Full API & more examples:** https://primeng.org/contextmenu
