# Services — MessageService, ConfirmationService, DialogService

Several PrimeNG features are driven by injectable services. **Each must be provided** (component `providers` or app-level) and usually paired with a host component in the template.

## `MessageService` → Toast / Message

Provide `MessageService`, render `<p-toast />` once, then call `add()`. See [components/toast.md](components/toast.md).

```ts
import { Component, inject } from "@angular/core";
import { ToastModule } from "primeng/toast";
import { MessageService } from "primeng/api";

@Component({
  standalone: true,
  imports: [ToastModule],
  providers: [MessageService],
  template: `<p-toast /> <p-button label="Save" (onClick)="save()" />`,
})
export class DemoComponent {
  private messages = inject(MessageService);
  save() {
    this.messages.add({
      severity: "success",
      summary: "Saved",
      detail: "Record updated",
      life: 3000,
    });
  }
}
```

- `severity`: `success | info | warn | error | secondary | contrast`.
- Target a specific `<p-toast key="...">` with the message `key`.
- `clear(key?)` removes messages.

## `ConfirmationService` → ConfirmDialog / ConfirmPopup

Provide `ConfirmationService`, render `<p-confirmdialog />` (or `<p-confirmpopup />`) once, call `confirm()` with `accept`/`reject` callbacks. See [components/confirmdialog.md](components/confirmdialog.md), [components/confirmpopup.md](components/confirmpopup.md).

```ts
import { ConfirmationService } from "primeng/api";
import { ConfirmDialogModule } from "primeng/confirmdialog";

@Component({
  standalone: true,
  imports: [ConfirmDialogModule],
  providers: [ConfirmationService],
  template: `<p-confirmdialog />
    <p-button label="Delete" (onClick)="remove($event)" />`,
})
export class DemoComponent {
  private confirm = inject(ConfirmationService);
  remove(event: Event) {
    this.confirm.confirm({
      target: event.target as EventTarget,
      message: "Are you sure?",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        /* … */
      },
      reject: () => {
        /* … */
      },
    });
  }
}
```

## `DialogService` → DynamicDialog

Open any component as a dialog at runtime. Provide `DialogService`, call `open(Component, config)`; it returns a `DynamicDialogRef`. Inside the opened component, inject `DynamicDialogConfig` (for `data`) and `DynamicDialogRef` (to `close(result)`). See [components/dynamicdialog.md](components/dynamicdialog.md).

```ts
import { DialogService, DynamicDialogRef } from "primeng/dynamicdialog";

@Component({
  standalone: true,
  providers: [DialogService],
  template: `<p-button label="Open" (onClick)="show()" />`,
})
export class DemoComponent {
  private dialog = inject(DialogService);
  private ref?: DynamicDialogRef;
  show() {
    this.ref = this.dialog.open(ProductListComponent, {
      header: "Choose a product",
      width: "70%",
      data: { id: 1 },
    });
    this.ref.onClose.subscribe((product) => {
      /* … */
    });
  }
}
```

```ts
// inside ProductListComponent
import { DynamicDialogConfig, DynamicDialogRef } from "primeng/dynamicdialog";
private config = inject(DynamicDialogConfig);   // this.config.data
private ref = inject(DynamicDialogRef);          // this.ref.close(selected)
```

> Provide these services at the **component** level (not always root) when their lifetime/keys should be scoped to a feature.
