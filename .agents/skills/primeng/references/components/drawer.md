# Drawer (`p-drawer`)

Drawer is a container component displayed as an overlay.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { DrawerModule } from "primeng/drawer";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { DrawerModule } from "primeng/drawer";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-drawer [(visible)]="visible" header="Drawer">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
      </p-drawer>
      <p-button (click)="visible = true" icon="pi pi-arrow-right" />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, DrawerModule],
})
export class DrawerBasicDemo {
  visible: boolean = false;
}
```

## Inputs

| Name             | Type                                                          | Default | Description                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appendTo         | InputSignal<any>                                              | 'self'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions    | InputSignal<MotionOptions>                                    | ...     | The motion options.                                                                                                                                                                                                                                  |
| blockScroll      | boolean                                                       | false   | Whether to block scrolling of the document when drawer is active.                                                                                                                                                                                    |
| style            | { [klass: string]: any }                                      | -       | Inline style of the component.                                                                                                                                                                                                                       |
| styleClass       | string                                                        | -       | Style class of the component.                                                                                                                                                                                                                        |
| ariaCloseLabel   | string                                                        | -       | Aria label of the close icon.                                                                                                                                                                                                                        |
| autoZIndex       | boolean                                                       | true    | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex       | number                                                        | 0       | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| modal            | boolean                                                       | true    | Whether an overlay mask is displayed behind the drawer.                                                                                                                                                                                              |
| closeButtonProps | ButtonProps                                                   | ...     | Used to pass all properties of the ButtonProps to the Button component.                                                                                                                                                                              |
| dismissible      | boolean                                                       | true    | Whether to dismiss drawer on click of the mask.                                                                                                                                                                                                      |
| closeOnEscape    | boolean                                                       | true    | Specifies if pressing escape key should hide the drawer.                                                                                                                                                                                             |
| visible          | boolean                                                       | -       | The visible property is an input that determines the visibility of the component.                                                                                                                                                                    |
| position         | InputSignal<"right" \| "left" \| "top" \| "bottom" \| "full"> | 'left'  | Specifies the position of the drawer, valid values are "left", "right", "bottom" and "top".                                                                                                                                                          |
| fullScreen       | InputSignal<boolean>                                          | false   | Adds a close icon to the header to hide the dialog.                                                                                                                                                                                                  |
| header           | string                                                        | -       | Title content of the dialog.                                                                                                                                                                                                                         |
| maskStyle        | { [klass: string]: any }                                      | -       | Style of the mask.                                                                                                                                                                                                                                   |
| closable         | boolean                                                       | true    | Whether to display close button.                                                                                                                                                                                                                     |

## Outputs

| Name          | Parameters     | Description                                           |
| ------------- | -------------- | ----------------------------------------------------- |
| onShow        | value: any     | Callback to invoke when dialog is shown.              |
| onHide        | value: any     | Callback to invoke when dialog is hidden.             |
| visibleChange | value: boolean | Callback to invoke when dialog visibility is changed. |

## Templates

| Name      | Type              | Description                                                    |
| --------- | ----------------- | -------------------------------------------------------------- |
| header    | TemplateRef<void> | Custom header template.                                        |
| footer    | TemplateRef<void> | Custom footer template.                                        |
| content   | TemplateRef<void> | Custom content template.                                       |
| closeicon | TemplateRef<void> | Custom close icon template.                                    |
| headless  | TemplateRef<void> | Custom headless template to replace the entire drawer content. |

**Full API & more examples:** https://primeng.org/drawer
