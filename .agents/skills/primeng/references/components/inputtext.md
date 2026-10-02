# InputText (`pInputText`)

InputText is an extension to standard input element with theming and keyfiltering.

**Import:**

```ts
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <input type="text" pInputText [(ngModel)]="value" />
    </div>
  `,
  standalone: true,
  imports: [InputTextModule, FormsModule],
})
export class InputtextBasicDemo {
  value: string;
}
```

## Inputs

| Name               | Type                                       | Default   | Description                                                                    |
| ------------------ | ------------------------------------------ | --------- | ------------------------------------------------------------------------------ |
| pInputTextPT       | InputSignal<InputTextPassThrough>          | undefined | Used to pass attributes to DOM elements inside the InputText component.        |
| pInputTextUnstyled | InputSignal<boolean>                       | undefined | Indicates whether the component should be rendered without styles.             |
| pSize              | "small" \| "large"                         | -         | Defines the size of the component.                                             |
| variant            | InputSignal<"outlined" \| "filled">        | undefined | Specifies the input variant of the component.                                  |
| fluid              | InputSignalWithTransform<boolean, unknown> | undefined | Spans 100% width of the container when enabled.                                |
| invalid            | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style. |

**Full API & more examples:** https://primeng.org/inputtext
