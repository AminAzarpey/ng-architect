# ConfirmPopup (`p-confirmpopup`)

ConfirmPopup displays a confirmation overlay displayed relatively to its target.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { ConfirmPopupModule } from "primeng/confirmpopup";
import { ToastModule } from "primeng/toast";
import { MessageService, ConfirmationService } from "primeng/api";
```

## Example

```typescript
import { Component, inject } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { ConfirmPopupModule } from "primeng/confirmpopup";
import { ToastModule } from "primeng/toast";
import { MessageService, ConfirmationService } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center gap-2">
      <p-toast />
      <p-confirmpopup />
      <p-button (onClick)="confirm1($event)" label="Save" [outlined]="true" />
      <p-button
        (onClick)="confirm2($event)"
        label="Delete"
        severity="danger"
        [outlined]="true"
      />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, ConfirmPopupModule, ToastModule],
  providers: [ConfirmationService, MessageService],
})
export class ConfirmpopupBasicDemo {
  private confirmationService = inject(ConfirmationService);
  private messageService = inject(MessageService);

  confirm2(event: Event) {
    this.confirmationService.confirm({
      target: event.currentTarget as EventTarget,
      message: "Do you want to delete this record?",
      icon: "pi pi-info-circle",
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
          life: 3000,
        });
      },
      reject: () => {
        this.messageService.add({
          severity: "error",
          summary: "Rejected",
          detail: "You have rejected",
          life: 3000,
        });
      },
    });
  }
}
```

## Inputs

| Name          | Type                       | Default | Description                                                                                                                                                                                                                                          |
| ------------- | -------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key           | string                     | -       | Optional key to match the key of confirm object, necessary to use when component tree has multiple confirm dialogs.                                                                                                                                  |
| defaultFocus  | string                     | accept  | Element to receive the focus when the popup gets visible, valid values are "accept", "reject", and "none".                                                                                                                                           |
| autoZIndex    | boolean                    | true    | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex    | number                     | 0       | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| style         | { [klass: string]: any }   | -       | Inline style of the component.                                                                                                                                                                                                                       |
| styleClass    | string                     | -       | Style class of the component.                                                                                                                                                                                                                        |
| visible       | InputSignal<boolean>       | ...     | Defines if the component is visible.                                                                                                                                                                                                                 |
| motionOptions | InputSignal<MotionOptions> | ...     | The motion options.                                                                                                                                                                                                                                  |
| appendTo      | InputSignal<any>           | 'body'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |

## Templates

| Name       | Type                                             | Description                  |
| ---------- | ------------------------------------------------ | ---------------------------- |
| content    | TemplateRef<ConfirmPopupContentTemplateContext>  | Custom content template.     |
| accepticon | TemplateRef<void>                                | Custom accept icon template. |
| rejecticon | TemplateRef<void>                                | Custom reject icon template. |
| headless   | TemplateRef<ConfirmPopupHeadlessTemplateContext> | Custom headless template.    |

**Full API & more examples:** https://primeng.org/confirmpopup
