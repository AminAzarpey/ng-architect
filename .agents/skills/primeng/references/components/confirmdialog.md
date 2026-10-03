# ConfirmDialog (`p-confirmdialog`)

ConfirmDialog is backed by a service utilizing Observables to display confirmation windows easily that can be shared by multiple actions on the same component.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { ConfirmDialogModule } from "primeng/confirmdialog";
import { ToastModule } from "primeng/toast";
import { MessageService, ConfirmationService } from "primeng/api";
```

## Example

```typescript
import { Component, inject } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { ConfirmDialogModule } from "primeng/confirmdialog";
import { ToastModule } from "primeng/toast";
import { MessageService, ConfirmationService } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center gap-2">
      <p-toast />
      <p-confirmdialog />
      <p-button (click)="confirm1($event)" label="Save" [outlined]="true" />
      <p-button
        (click)="confirm2($event)"
        label="Delete"
        severity="danger"
        [outlined]="true"
      />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, ConfirmDialogModule, ToastModule],
  providers: [ConfirmationService, MessageService],
})
export class ConfirmdialogBasicDemo {
  private confirmationService = inject(ConfirmationService);
  private messageService = inject(MessageService);

  confirm2(event: Event) {
    this.confirmationService.confirm({
      target: event.target as EventTarget,
      message: "Do you want to delete this record?",
      header: "Danger Zone",
      icon: "pi pi-info-circle",
      rejectLabel: "Cancel",
      rejectButtonProps: {
        label: "Cancel",
        severity: "secondary",
        outlined: true,
      },
      acceptButtonProps: {
        label: "Delete",
        severity: "danger",
      },

      accept: () => {
        this.messageService.add({
          severity: "info",
          summary: "Confirmed",
          detail: "Record deleted",
        });
      },
      reject: () => {
        this.messageService.add({
          severity: "error",
          summary: "Rejected",
          detail: "You have rejected",
        });
      },
    });
  }
}
```

## Inputs

| Name                   | Type                                                                                                           | Default                          | Description                                                                                                                                                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| header                 | string                                                                                                         | -                                | Title text of the dialog.                                                                                                                                                                                                                            |
| icon                   | string                                                                                                         | -                                | Icon to display next to message.                                                                                                                                                                                                                     |
| message                | string                                                                                                         | -                                | Message of the confirmation.                                                                                                                                                                                                                         |
| style                  | { [klass: string]: any }                                                                                       | -                                | Inline style of the element.                                                                                                                                                                                                                         |
| styleClass             | string                                                                                                         | -                                | Class of the element.                                                                                                                                                                                                                                |
| maskStyleClass         | string                                                                                                         | -                                | Specify the CSS class(es) for styling the mask element                                                                                                                                                                                               |
| acceptIcon             | string                                                                                                         | -                                | Icon of the accept button.                                                                                                                                                                                                                           |
| acceptLabel            | string                                                                                                         | -                                | Label of the accept button.                                                                                                                                                                                                                          |
| closeAriaLabel         | string                                                                                                         | -                                | Defines a string that labels the close button for accessibility.                                                                                                                                                                                     |
| acceptAriaLabel        | string                                                                                                         | -                                | Defines a string that labels the accept button for accessibility.                                                                                                                                                                                    |
| acceptVisible          | boolean                                                                                                        | true                             | Visibility of the accept button.                                                                                                                                                                                                                     |
| rejectIcon             | string                                                                                                         | -                                | Icon of the reject button.                                                                                                                                                                                                                           |
| rejectLabel            | string                                                                                                         | -                                | Label of the reject button.                                                                                                                                                                                                                          |
| rejectAriaLabel        | string                                                                                                         | -                                | Defines a string that labels the reject button for accessibility.                                                                                                                                                                                    |
| rejectVisible          | boolean                                                                                                        | true                             | Visibility of the reject button.                                                                                                                                                                                                                     |
| acceptButtonStyleClass | string                                                                                                         | -                                | Style class of the accept button.                                                                                                                                                                                                                    |
| rejectButtonStyleClass | string                                                                                                         | -                                | Style class of the reject button.                                                                                                                                                                                                                    |
| closeOnEscape          | boolean                                                                                                        | true                             | Specifies if pressing escape key should hide the dialog.                                                                                                                                                                                             |
| dismissableMask        | boolean                                                                                                        | false                            | Specifies if clicking the modal background should hide the dialog.                                                                                                                                                                                   |
| blockScroll            | boolean                                                                                                        | true                             | Determines whether scrolling behavior should be blocked within the component.                                                                                                                                                                        |
| rtl                    | boolean                                                                                                        | false                            | When enabled dialog is displayed in RTL direction.                                                                                                                                                                                                   |
| closable               | boolean                                                                                                        | true                             | Adds a close icon to the header to hide the dialog.                                                                                                                                                                                                  |
| appendTo               | InputSignal<any>                                                                                               | 'body'                           | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| key                    | string                                                                                                         | -                                | Optional key to match the key of confirm object, necessary to use when component tree has multiple confirm dialogs.                                                                                                                                  |
| autoZIndex             | boolean                                                                                                        | true                             | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex             | number                                                                                                         | 0                                | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| transitionOptions      | string                                                                                                         | 150ms cubic-bezier(0, 0, 0.2, 1) | Transition options of the animation.                                                                                                                                                                                                                 |
| focusTrap              | boolean                                                                                                        | true                             | When enabled, can only focus on elements inside the confirm dialog.                                                                                                                                                                                  |
| defaultFocus           | "accept" \| "reject" \| "none" \| "close"                                                                      | accept                           | Element to receive the focus when the dialog gets visible.                                                                                                                                                                                           |
| breakpoints            | any                                                                                                            | -                                | Object literal to define widths per screen size.                                                                                                                                                                                                     |
| modal                  | boolean                                                                                                        | true                             | Defines if background should be blocked when dialog is displayed.                                                                                                                                                                                    |
| visible                | any                                                                                                            | -                                | Current visible state as a boolean.                                                                                                                                                                                                                  |
| position               | "right" \| "left" \| "top" \| "bottom" \| "center" \| "topleft" \| "bottomleft" \| "topright" \| "bottomright" | center                           | Allows getting the position of the component.                                                                                                                                                                                                        |
| draggable              | boolean                                                                                                        | true                             | Enables dragging to change the position using header.                                                                                                                                                                                                |

## Outputs

| Name   | Parameters              | Description                               |
| ------ | ----------------------- | ----------------------------------------- |
| onHide | event: ConfirmEventType | Callback to invoke when dialog is hidden. |

## Templates

| Name       | Type                                              | Description                  |
| ---------- | ------------------------------------------------- | ---------------------------- |
| header     | TemplateRef<void>                                 | Custom header template.      |
| footer     | TemplateRef<void>                                 | Custom footer template.      |
| rejecticon | TemplateRef<void>                                 | Custom reject icon template. |
| accepticon | TemplateRef<void>                                 | Custom accept icon template. |
| message    | TemplateRef<ConfirmDialogMessageTemplateContext>  | Custom message template.     |
| icon       | TemplateRef<void>                                 | Custom icon template.        |
| headless   | TemplateRef<ConfirmDialogHeadlessTemplateContext> | Custom headless template.    |

**Full API & more examples:** https://primeng.org/confirmdialog
