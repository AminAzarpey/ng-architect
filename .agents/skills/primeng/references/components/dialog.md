# Dialog (`p-dialog`)

Dialog is a container to display content in an overlay window.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { DialogModule } from "primeng/dialog";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { DialogModule } from "primeng/dialog";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-button (click)="showDialog()" label="Show" />
      <p-dialog
        header="Edit Profile"
        [modal]="true"
        [(visible)]="visible"
        [style]="{ width: '25rem' }"
      >
        <span class="p-text-secondary block mb-8"
          >Update your information.</span
        >
        <div class="flex items-center gap-4 mb-4">
          <label for="username" class="font-semibold w-24">Username</label>
          <input
            pInputText
            id="username"
            class="flex-auto"
            autocomplete="off"
          />
        </div>
        <div class="flex items-center gap-4 mb-8">
          <label for="email" class="font-semibold w-24">Email</label>
          <input pInputText id="email" class="flex-auto" autocomplete="off" />
        </div>
        <div class="flex justify-end gap-2">
          <p-button
            label="Cancel"
            severity="secondary"
            (click)="visible = false"
          />
          <p-button label="Save" (click)="visible = false" />
        </div>
      </p-dialog>
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, DialogModule, InputTextModule],
})
export class DialogBasicDemo {
  visible: boolean = false;

  showDialog() {
    this.visible = true;
  }
}
```

## Inputs

| Name                | Type                                                                                                           | Default | Description                                                                                                                                                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| header              | string                                                                                                         | -       | Title text of the dialog.                                                                                                                                                                                                                            |
| draggable           | boolean                                                                                                        | true    | Enables dragging to change the position using header.                                                                                                                                                                                                |
| resizable           | boolean                                                                                                        | true    | Enables resizing of the content.                                                                                                                                                                                                                     |
| contentStyle        | any                                                                                                            | -       | Style of the content section.                                                                                                                                                                                                                        |
| contentStyleClass   | string                                                                                                         | -       | Style class of the content.                                                                                                                                                                                                                          |
| modal               | boolean                                                                                                        | false   | Defines if background should be blocked when dialog is displayed.                                                                                                                                                                                    |
| closeOnEscape       | boolean                                                                                                        | true    | Specifies if pressing escape key should hide the dialog.                                                                                                                                                                                             |
| dismissableMask     | boolean                                                                                                        | false   | Specifies if clicking the modal background should hide the dialog.                                                                                                                                                                                   |
| rtl                 | boolean                                                                                                        | false   | When enabled dialog is displayed in RTL direction.                                                                                                                                                                                                   |
| closable            | boolean                                                                                                        | true    | Adds a close icon to the header to hide the dialog.                                                                                                                                                                                                  |
| breakpoints         | any                                                                                                            | -       | Object literal to define widths per screen size.                                                                                                                                                                                                     |
| styleClass          | string                                                                                                         | -       | Style class of the component.                                                                                                                                                                                                                        |
| maskStyleClass      | string                                                                                                         | -       | Style class of the mask.                                                                                                                                                                                                                             |
| maskStyle           | { [klass: string]: any }                                                                                       | -       | Style of the mask.                                                                                                                                                                                                                                   |
| showHeader          | boolean                                                                                                        | true    | Whether to show the header or not.                                                                                                                                                                                                                   |
| blockScroll         | boolean                                                                                                        | false   | Whether background scroll should be blocked when dialog is visible.                                                                                                                                                                                  |
| autoZIndex          | boolean                                                                                                        | true    | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex          | number                                                                                                         | 0       | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| minX                | number                                                                                                         | 0       | Minimum value for the left coordinate of dialog in dragging.                                                                                                                                                                                         |
| minY                | number                                                                                                         | 0       | Minimum value for the top coordinate of dialog in dragging.                                                                                                                                                                                          |
| focusOnShow         | boolean                                                                                                        | true    | When enabled, first focusable element receives focus on show.                                                                                                                                                                                        |
| maximizable         | boolean                                                                                                        | false   | Whether the dialog can be displayed full screen.                                                                                                                                                                                                     |
| keepInViewport      | boolean                                                                                                        | true    | Keeps dialog in the viewport.                                                                                                                                                                                                                        |
| focusTrap           | boolean                                                                                                        | true    | When enabled, can only focus on elements inside the dialog.                                                                                                                                                                                          |
| maskMotionOptions   | InputSignal<MotionOptions>                                                                                     | ...     | The motion options for the mask.                                                                                                                                                                                                                     |
| motionOptions       | InputSignal<MotionOptions>                                                                                     | ...     | The motion options.                                                                                                                                                                                                                                  |
| closeIcon           | string                                                                                                         | -       | Name of the close icon.                                                                                                                                                                                                                              |
| closeAriaLabel      | string                                                                                                         | -       | Defines a string that labels the close button for accessibility.                                                                                                                                                                                     |
| closeTabindex       | string                                                                                                         | 0       | Index of the close button in tabbing order.                                                                                                                                                                                                          |
| minimizeIcon        | string                                                                                                         | -       | Name of the minimize icon.                                                                                                                                                                                                                           |
| maximizeIcon        | string                                                                                                         | -       | Name of the maximize icon.                                                                                                                                                                                                                           |
| closeButtonProps    | ButtonProps                                                                                                    | ...     | Used to pass all properties of the ButtonProps to the Button component.                                                                                                                                                                              |
| maximizeButtonProps | ButtonProps                                                                                                    | ...     | Used to pass all properties of the ButtonProps to the Button component.                                                                                                                                                                              |
| visible             | boolean                                                                                                        | -       | Specifies the visibility of the dialog.                                                                                                                                                                                                              |
| style               | any                                                                                                            | -       | Inline style of the component.                                                                                                                                                                                                                       |
| position            | "right" \| "left" \| "top" \| "bottom" \| "center" \| "topleft" \| "bottomleft" \| "topright" \| "bottomright" | -       | Position of the dialog.                                                                                                                                                                                                                              |
| appendTo            | InputSignal<any>                                                                                               | 'self'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |

## Outputs

| Name          | Parameters        | Description                                                                         |
| ------------- | ----------------- | ----------------------------------------------------------------------------------- |
| role          | value: undefined  | Role attribute of html element.                                                     |
| onShow        | value: any        | Callback to invoke when dialog is shown.                                            |
| onHide        | value: any        | Callback to invoke when dialog is hidden.                                           |
| visibleChange | value: boolean    | This EventEmitter is used to notify changes in the visibility state of a component. |
| onResizeInit  | event: MouseEvent | Callback to invoke when dialog resizing is initiated.                               |
| onResizeEnd   | event: MouseEvent | Callback to invoke when dialog resizing is completed.                               |
| onDragEnd     | event: DragEvent  | Callback to invoke when dialog dragging is completed.                               |
| onMaximize    | value: any        | Callback to invoke when dialog maximized or unmaximized.                            |

## Templates

| Name           | Type              | Description                    |
| -------------- | ----------------- | ------------------------------ |
| header         | TemplateRef<void> | Header template.               |
| content        | TemplateRef<void> | Content template.              |
| footer         | TemplateRef<void> | Footer template.               |
| closeicon      | TemplateRef<void> | Close icon template.           |
| maximizeicon   | TemplateRef<void> | Maximize icon template.        |
| minimizeicon   | TemplateRef<void> | Minimize icon template.        |
| headless       | TemplateRef<void> | Headless template.             |
| \_header       | TemplateRef<void> | Custom header template.        |
| \_content      | TemplateRef<void> | Custom content template.       |
| \_footer       | TemplateRef<void> | Custom footer template.        |
| \_closeicon    | TemplateRef<void> | Custom close icon template.    |
| \_maximizeicon | TemplateRef<void> | Custom maximize icon template. |
| \_minimizeicon | TemplateRef<void> | Custom minimize icon template. |
| \_headless     | TemplateRef<void> | Custom headless template.      |

**Full API & more examples:** https://primeng.org/dialog
