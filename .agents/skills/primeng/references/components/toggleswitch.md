# ToggleSwitch (`p-toggleswitch`)

ToggleSwitch is used to select a boolean value.

**Import:**

```ts
import { ToggleSwitchModule } from "primeng/toggleswitch";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { ToggleSwitchModule } from "primeng/toggleswitch";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-toggleswitch [(ngModel)]="checked" />
    </div>
  `,
  standalone: true,
  imports: [ToggleSwitchModule, FormsModule],
})
export class ToggleswitchBasicDemo {
  checked: boolean = false;
}
```

**Full API & more examples:** https://primeng.org/toggleswitch
