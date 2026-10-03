# Dynamic Dialog

Dialogs can be created dynamically with any component as the content using a DialogService.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { ToastModule } from "primeng/toast";
import { MessageService, DialogService } from "primeng/api";
import { Dialog } from "primeng/dialog";
```

## Example

```typescript
import { Component, inject } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { ToastModule } from "primeng/toast";
import { MessageService, DialogService } from "primeng/api";
import { Product } from "@/domain/product";
import { Dialog } from "primeng/dialog";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-toast />
      <p-button (click)="show()" icon="pi pi-search" label="Select a Product" />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, ToastModule],
  providers: [DialogService, MessageService],
})
export class DynamicdialogExampleDemo {
  private dialogService = inject(DialogService);
  private messageService = inject(MessageService);

  show() {
    this.ref = this.dialogService.open(ProductListDemo, {
      header: "Product List",
      modal: true,
      width: "50vw",
      closable: true,
      contentStyle: { overflow: "auto" },
      breakpoints: {
        "960px": "75vw",
        "640px": "90vw",
      },
      templates: {
        footer: Footer,
      },
    });

    this.ref.onClose.subscribe((data: any) => {
      let summary_and_detail;
      if (data) {
        const buttonType = data?.buttonType;
        summary_and_detail = buttonType
          ? {
              summary: "No Product Selected",
              detail: `Pressed '${buttonType}' button`,
            }
          : { summary: "Product Selected", detail: data?.name };
      } else {
        summary_and_detail = {
          summary: "No Product Selected",
          detail: "Pressed Close button",
        };
      }
      this.messageService.add({
        severity: "info",
        ...summary_and_detail,
        life: 3000,
      });
    });

    this.ref.onMaximize.subscribe((value) => {
      this.messageService.add({
        severity: "info",
        summary: "Maximized",
        detail: `maximized: ${value.maximized}`,
      });
    });
  }
}
```

**Full API & more examples:** https://primeng.org/dynamicdialog
