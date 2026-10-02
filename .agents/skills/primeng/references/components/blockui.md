# BlockUI (`p-blockui`)

BlockUI can either block other components or the whole page.

**Import:**

```ts
import { BlockUIModule } from "primeng/blockui";
import { ButtonModule } from "primeng/button";
import { PanelModule } from "primeng/panel";
```

## Example

```typescript
import { Component } from "@angular/core";
import { BlockUIModule } from "primeng/blockui";
import { ButtonModule } from "primeng/button";
import { PanelModule } from "primeng/panel";

@Component({
  template: `
    <div class="card">
      <p-button
        label="Block"
        (click)="blockedPanel = true"
        class="me-2"
        severity="secondary"
      />
      <p-button
        label="Unblock"
        (click)="blockedPanel = false"
        severity="secondary"
      />
      <p-blockui [target]="pnl" [blocked]="blockedPanel" />
      <p-panel #pnl header="Header" class="mt-6">
        <p class="m-0">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </p-panel>
    </div>
  `,
  standalone: true,
  imports: [BlockUIModule, ButtonModule, PanelModule],
})
export class BlockuiBasicDemo {
  blockedPanel: boolean = false;
}
```

## Inputs

| Name       | Type    | Default | Description                                                            |
| ---------- | ------- | ------- | ---------------------------------------------------------------------- |
| target     | any     | -       | Name of the local ng-template variable referring to another component. |
| autoZIndex | boolean | true    | Whether to automatically manage layering.                              |
| baseZIndex | number  | 0       | Base zIndex value to use in layering.                                  |
| blocked    | boolean | -       | Current blocked state as a boolean.                                    |

## Templates

| Name    | Type             | Description             |
| ------- | ---------------- | ----------------------- |
| content | TemplateRef<any> | template of the content |

**Full API & more examples:** https://primeng.org/blockui
