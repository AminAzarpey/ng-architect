# Toolbar (`p-toolbar`)

Toolbar is a grouping component for buttons and other content.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { IconFieldModule } from "primeng/iconfield";
import { InputIconModule } from "primeng/inputicon";
import { SplitButtonModule } from "primeng/splitbutton";
import { ToolbarModule } from "primeng/toolbar";
import { InputTextModule } from "primeng/inputtext";
import { MenuItem } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { IconFieldModule } from "primeng/iconfield";
import { InputIconModule } from "primeng/inputicon";
import { SplitButtonModule } from "primeng/splitbutton";
import { ToolbarModule } from "primeng/toolbar";
import { InputTextModule } from "primeng/inputtext";
import { MenuItem } from "primeng/api";

@Component({
  template: `
    <div class="card">
      <p-toolbar>
        <ng-template #start>
          <p-button icon="pi pi-plus" class="mr-2" text severity="secondary" />
          <p-button icon="pi pi-print" class="mr-2" text severity="secondary" />
          <p-button icon="pi pi-upload" text severity="secondary" />
        </ng-template>
        <ng-template #center>
          <p-iconfield iconPosition="left">
            <p-inputicon class="pi pi-search" />
            <input type="text" pInputText placeholder="Search" />
          </p-iconfield>
        </ng-template>
        <ng-template #end>
          <p-splitbutton label="Save" [model]="items" />
        </ng-template>
      </p-toolbar>
    </div>
  `,
  standalone: true,
  imports: [
    ButtonModule,
    IconFieldModule,
    InputIconModule,
    SplitButtonModule,
    ToolbarModule,
    InputTextModule,
  ],
})
export class ToolbarBasicDemo implements OnInit {
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      {
        label: "Update",
        icon: "pi pi-refresh",
      },
      {
        label: "Delete",
        icon: "pi pi-times",
      },
    ];
  }
}
```

## Inputs

| Name           | Type   | Default | Description                                                |
| -------------- | ------ | ------- | ---------------------------------------------------------- |
| ariaLabelledBy | string | -       | Defines a string value that labels an interactive element. |

## Templates

| Name   | Type              | Description             |
| ------ | ----------------- | ----------------------- |
| start  | TemplateRef<void> | Custom start template.  |
| end    | TemplateRef<void> | Custom end template.    |
| center | TemplateRef<void> | Custom center template. |

**Full API & more examples:** https://primeng.org/toolbar
