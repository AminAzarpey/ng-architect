# AutoFocus (`pAutoFocus`)

AutoFocus manages focus on focusable element on load.

**Import:**

```ts
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <input
        type="text"
        pInputText
        [pAutoFocus]="true"
        placeholder="Automatically focused"
      />
    </div>
  `,
  standalone: true,
  imports: [InputTextModule],
})
export class AutofocusBasicDemo {}
```

## Inputs

| Name      | Type    | Default | Description                                                                           |
| --------- | ------- | ------- | ------------------------------------------------------------------------------------- |
| autofocus | boolean | false   | When present, it specifies that the component should automatically get focus on load. |

**Full API & more examples:** https://primeng.org/autofocus
