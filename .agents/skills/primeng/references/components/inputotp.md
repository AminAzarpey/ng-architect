# Otp Input (`p-inputotp`)

Input Otp is used to enter one time passwords.

**Import:**

```ts
import { InputOtpModule } from "primeng/inputotp";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { InputOtpModule } from "primeng/inputotp";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-inputotp [(ngModel)]="value" />
    </div>
  `,
  standalone: true,
  imports: [InputOtpModule, FormsModule],
})
export class InputotpBasicDemo {
  value: any;
}
```

## Inputs

| Name        | Type                                       | Default   | Description                                                                           |
| ----------- | ------------------------------------------ | --------- | ------------------------------------------------------------------------------------- |
| required    | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                       |
| invalid     | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.        |
| disabled    | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.       |
| name        | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                |
| readonly    | boolean                                    | false     | When present, it specifies that an input field is read-only.                          |
| tabindex    | number                                     | null      | Index of the element in tabbing order.                                                |
| length      | number                                     | 4         | Number of characters to initiate.                                                     |
| styleClass  | string                                     | -         | Style class of the input element.                                                     |
| mask        | boolean                                    | false     | Mask pattern.                                                                         |
| integerOnly | boolean                                    | false     | When present, it specifies that an input field is integer-only.                       |
| autofocus   | boolean                                    | false     | When present, it specifies that the component should automatically get focus on load. |
| variant     | InputSignal<"outlined" \| "filled">        | undefined | Specifies the input variant of the component.                                         |
| size        | InputSignal<"small" \| "large">            | undefined | Specifies the size of the component.                                                  |

## Outputs

| Name     | Parameters                 | Description                                           |
| -------- | -------------------------- | ----------------------------------------------------- |
| onChange | event: InputOtpChangeEvent | Callback to invoke on value change.                   |
| onFocus  | event: Event               | Callback to invoke when the component receives focus. |
| onBlur   | event: Event               | Callback to invoke when the component loses focus.    |

## Templates

| Name  | Type                                      | Description            |
| ----- | ----------------------------------------- | ---------------------- |
| input | TemplateRef<InputOtpInputTemplateContext> | Custom input template. |

**Full API & more examples:** https://primeng.org/inputotp
