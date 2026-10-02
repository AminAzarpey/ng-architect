# RadioButton (`p-radiobutton`)

RadioButton is an extension to standard radio button element with theming.

**Import:**

```ts
import { RadioButtonModule } from "primeng/radiobutton";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { RadioButtonModule } from "primeng/radiobutton";

@Component({
  template: `
    <div class="card flex justify-center gap-2">
      <p-radiobutton [(ngModel)]="value" [value]="1" [disabled]="true" />
      <p-radiobutton [(ngModel)]="value" [value]="2" [disabled]="true" />
    </div>
  `,
  standalone: true,
  imports: [RadioButtonModule, FormsModule],
})
export class RadiobuttonDisabledDemo {
  value: number = 2;
}
```

**Full API & more examples:** https://primeng.org/radiobutton
