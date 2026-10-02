# Float Label (`p-floatlabel`)

FloatLabel appears on top of the input field when focused.

**Import:**

```ts
import { FloatLabelModule } from "primeng/floatlabel";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { FloatLabelModule } from "primeng/floatlabel";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-floatlabel>
        <input
          id="username"
          pInputText
          [(ngModel)]="value"
          autocomplete="off"
        />
        <label for="username">Username</label>
      </p-floatlabel>
    </div>
  `,
  standalone: true,
  imports: [FloatLabelModule, InputTextModule, FormsModule],
})
export class FloatlabelBasicDemo {
  value: string | undefined;
}
```

## Inputs

| Name    | Type                   | Default | Description                                                 |
| ------- | ---------------------- | ------- | ----------------------------------------------------------- |
| variant | "in" \| "on" \| "over" | over    | Defines the positioning of the label relative to the input. |

**Full API & more examples:** https://primeng.org/floatlabel
