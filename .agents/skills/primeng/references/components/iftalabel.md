# Ifta Label (`p-iftalabel`)

IftaLabel is used to create infield top aligned labels.

**Import:**

```ts
import { IftaLabelModule } from "primeng/iftalabel";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { IftaLabelModule } from "primeng/iftalabel";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-iftalabel>
        <input
          pInputText
          id="username"
          [(ngModel)]="value"
          autocomplete="off"
        />
        <label for="username">Username</label>
      </p-iftalabel>
    </div>
  `,
  standalone: true,
  imports: [IftaLabelModule, InputTextModule, FormsModule],
})
export class IftalabelBasicDemo {
  value: string | undefined;
}
```

**Full API & more examples:** https://primeng.org/iftalabel
