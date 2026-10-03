# Dock (`p-dock`)

Dock is a navigation component consisting of menuitems.

**Import:**

```ts
import { DockModule } from "primeng/dock";
import { RadioButtonModule } from "primeng/radiobutton";
import { TooltipModule } from "primeng/tooltip";
import { MenuItem } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { DockModule } from "primeng/dock";
import { RadioButtonModule } from "primeng/radiobutton";
import { TooltipModule } from "primeng/tooltip";
import { MenuItem } from "primeng/api";

@Component({
  template: `
    <div class="card">
      <div class="flex flex-wrap gap-4 mb-8">
        <div *ngFor="let pos of positionOptions" class="flex items-center">
          <p-radiobutton
            name="dock"
            [value]="pos.value"
            [label]="pos.label"
            [(ngModel)]="position"
            [inputId]="pos.label"
          />
          <label [for]="pos.label" class="ml-2"> {{ pos.label }} </label>
        </div>
      </div>
      <div class="dock-window">
        <p-dock [model]="items" [position]="position">
          <ng-template #item let-item>
            <img
              [pTooltip]="item.label"
              tooltipPosition="top"
              [src]="item.icon"
              [alt]="item.label"
              width="100%"
            />
          </ng-template>
        </p-dock>
      </div>
    </div>
  `,
  standalone: true,
  imports: [DockModule, RadioButtonModule, TooltipModule, FormsModule],
})
export class DockBasicDemo implements OnInit {
  items: MenuItem[] | undefined;
  positionOptions: any[];

  ngOnInit() {
    this.items = [
      {
        label: "Finder",
        icon: "https://primefaces.org/cdn/primeng/images/dock/finder.svg",
      },
      {
        label: "App Store",
        icon: "https://primefaces.org/cdn/primeng/images/dock/appstore.svg",
      },
      {
        label: "Photos",
        icon: "https://primefaces.org/cdn/primeng/images/dock/photos.svg",
      },
      {
        label: "Trash",
        icon: "https://primefaces.org/cdn/primeng/images/dock/trash.png",
      },
    ];
  }
}
```

## Inputs

| Name           | Type                                   | Default | Description                                                         |
| -------------- | -------------------------------------- | ------- | ------------------------------------------------------------------- |
| id             | string                                 | -       | Current id state as a string.                                       |
| model          | MenuItem[]                             | null    | MenuModel instance to define the action items.                      |
| position       | "right" \| "left" \| "top" \| "bottom" | bottom  | Position of element.                                                |
| ariaLabel      | string                                 | -       | Defines a string that labels the input for accessibility.           |
| breakpoint     | string                                 | 960px   | The breakpoint to define the maximum width boundary.                |
| ariaLabelledBy | string                                 | -       | Defines a string that labels the dropdown button for accessibility. |

## Outputs

| Name    | Parameters        | Description                                        |
| ------- | ----------------- | -------------------------------------------------- |
| onFocus | event: FocusEvent | Callback to execute when button is focused.        |
| onBlur  | event: FocusEvent | Callback to invoke when the component loses focus. |

## Templates

| Name | Type                                 | Description           |
| ---- | ------------------------------------ | --------------------- |
| item | TemplateRef<DockItemTemplateContext> | Custom item template. |

**Full API & more examples:** https://primeng.org/dock
