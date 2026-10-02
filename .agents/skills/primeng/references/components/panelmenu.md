# PanelMenu (`p-panelmenu`)

PanelMenu is a hybrid of Accordion and Tree components.

**Import:**

```ts
import { PanelMenu, PanelMenuModule } from "primeng/panelmenu";
import { MenuItem } from "primeng/api";
import { PanelMenu } from "primeng/panelmenu";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { PanelMenu, PanelMenuModule } from "primeng/panelmenu";
import { MenuItem } from "primeng/api";
import { PanelMenu } from "primeng/panelmenu";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-panelmenu [model]="items" class="w-full md:w-80" />
    </div>
  `,
  standalone: true,
  imports: [PanelMenuModule],
})
export class PanelmenuBasicDemo implements OnInit {
  items: MenuItem[];

  ngOnInit() {
    this.items = [
      {
        label: "Files",
        icon: "pi pi-file",
        items: [
          {
            label: "Documents",
            icon: "pi pi-file",
            items: [
              {
                label: "Invoices",
                icon: "pi pi-file-pdf",
                items: [
                  {
                    label: "Pending",
                    icon: "pi pi-stop",
                  },
                  {
                    label: "Paid",
                    icon: "pi pi-check-circle",
                  },
                ],
              },
              {
                label: "Clients",
                icon: "pi pi-users",
              },
            ],
          },
          {
            label: "Images",
            icon: "pi pi-image",
            items: [
              {
                label: "Logos",
                icon: "pi pi-image",
              },
            ],
          },
        ],
      },
      {
        label: "Cloud",
        icon: "pi pi-cloud",
        items: [
          {
            label: "Upload",
            icon: "pi pi-cloud-upload",
          },
          {
            label: "Download",
            icon: "pi pi-cloud-download",
          },
          {
            label: "Sync",
            icon: "pi pi-refresh",
          },
        ],
      },
      {
        label: "Devices",
        icon: "pi pi-desktop",
        items: [
          {
            label: "Phone",
            icon: "pi pi-mobile",
          },
          {
            label: "Desktop",
            icon: "pi pi-desktop",
          },
          {
            label: "Tablet",
            icon: "pi pi-tablet",
          },
        ],
      },
    ];
  }
}
```

## Inputs

| Name          | Type                       | Default | Description                                                     |
| ------------- | -------------------------- | ------- | --------------------------------------------------------------- |
| model         | MenuItem[]                 | -       | An array of menuitems.                                          |
| multiple      | boolean                    | false   | Whether multiple tabs can be activated at the same time or not. |
| motionOptions | InputSignal<MotionOptions> | ...     | The motion options.                                             |
| id            | string                     | -       | Current id state as a string.                                   |
| tabindex      | number                     | 0       | Index of the element in tabbing order.                          |

## Templates

| Name        | Type                                      | Description                      |
| ----------- | ----------------------------------------- | -------------------------------- |
| submenuicon | TemplateRef<void>                         | Template option of submenu icon. |
| headericon  | TemplateRef<void>                         | Template option of header icon.  |
| item        | TemplateRef<PanelMenuItemTemplateContext> | Template option of item.         |

## Methods

| Name        | Parameters | Return Type | Description            |
| ----------- | ---------- | ----------- | ---------------------- |
| collapseAll |            | void        | Collapses open panels. |

**Full API & more examples:** https://primeng.org/panelmenu
