# InputMask

InputMask component is used to enter input in a certain format such as numeric, date, currency and phone.

**Import:**

```ts
import { InputTextModule } from "primeng/inputtext";
import { InputMaskModule } from "primeng/inputmask";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { InputTextModule } from "primeng/inputtext";
import { InputMaskModule } from "primeng/inputmask";

@Component({
  template: `
    <div class="card flex justify-center">
      <input
        pInputText
        pInputMask="99-999999"
        [(ngModel)]="value"
        placeholder="99-999999"
      />
    </div>
  `,
  standalone: true,
  imports: [InputTextModule, InputMaskModule, FormsModule],
})
export class InputmaskBasicDemo {
  value: string | undefined;
}
```

## Inputs

| Name             | Type                                       | Default    | Description                                                                                                     |
| ---------------- | ------------------------------------------ | ---------- | --------------------------------------------------------------------------------------------------------------- |
| required         | InputSignalWithTransform<boolean, unknown> | false      | There must be a value (if set).                                                                                 |
| invalid          | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have invalid state style.                                  |
| disabled         | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have disabled state style.                                 |
| name             | InputSignal<string>                        | undefined  | When present, it specifies that the name of the input.                                                          |
| fluid            | InputSignalWithTransform<boolean, unknown> | false      | Spans 100% width of the container when enabled.                                                                 |
| variant          | InputSignal<"outlined" \| "filled">        | 'outlined' | Specifies the input variant of the component.                                                                   |
| size             | InputSignal<"small" \| "large">            | undefined  | Specifies the size of the component.                                                                            |
| inputSize        | InputSignal<number>                        | undefined  | Specifies the visible width of the input element in characters.                                                 |
| pattern          | InputSignal<string>                        | undefined  | Specifies the value must match the pattern.                                                                     |
| min              | InputSignal<number>                        | undefined  | The value must be greater than or equal to the value.                                                           |
| max              | InputSignal<number>                        | undefined  | The value must be less than or equal to the value.                                                              |
| step             | InputSignal<number>                        | undefined  | Unless the step is set to the any literal, the value must be min + an integral multiple of the step.            |
| minlength        | InputSignal<number>                        | undefined  | The number of characters (code points) must not be less than the value of the attribute, if non-empty.          |
| maxlength        | InputSignal<number>                        | undefined  | The number of characters (code points) must not exceed the value of the attribute.                              |
| type             | string                                     | text       | HTML5 input type.                                                                                               |
| slotChar         | string                                     | \_         | Placeholder character in mask, default is underscore.                                                           |
| autoClear        | boolean                                    | true       | Clears the incomplete value on blur.                                                                            |
| showClear        | boolean                                    | false      | When enabled, a clear icon is displayed to clear the value.                                                     |
| style            | { [klass: string]: any }                   | -          | Inline style of the input field.                                                                                |
| inputId          | string                                     | -          | Identifier of the focus input to match a label defined for the component.                                       |
| styleClass       | string                                     | -          | Style class of the input field.                                                                                 |
| placeholder      | string                                     | -          | Advisory information to display on input.                                                                       |
| tabindex         | string                                     | -          | Specifies tab order of the element.                                                                             |
| title            | string                                     | -          | Title text of the input text.                                                                                   |
| ariaLabel        | string                                     | -          | Used to define a string that labels the input element.                                                          |
| ariaLabelledBy   | string                                     | -          | Establishes relationships between the component and label(s) where its value should be one or more element IDs. |
| ariaRequired     | boolean                                    | false      | Used to indicate that user input is required on an element before a form can be submitted.                      |
| readonly         | boolean                                    | false      | When present, it specifies that an input field is read-only.                                                    |
| unmask           | boolean                                    | false      | Defines if ngModel sets the raw unmasked value to bound value or the formatted mask value.                      |
| characterPattern | string                                     | [A-Za-z]   | Regex pattern for alpha characters                                                                              |
| autofocus        | boolean                                    | false      | When present, the input gets a focus automatically on load.                                                     |
| autocomplete     | string                                     | -          | Used to define a string that autocomplete attribute the current element.                                        |
| keepBuffer       | boolean                                    | false      | When present, it specifies that whether to clean buffer value from model.                                       |
| mask             | string                                     | -          | Mask pattern.                                                                                                   |

## Outputs

| Name       | Parameters   | Description                                           |
| ---------- | ------------ | ----------------------------------------------------- |
| onComplete | value: any   | Callback to invoke when the mask is completed.        |
| onFocus    | event: Event | Callback to invoke when the component receives focus. |
| onBlur     | event: Event | Callback to invoke when the component loses focus.    |
| onInput    | event: Event | Callback to invoke on input.                          |
| onKeydown  | event: Event | Callback to invoke on input key press.                |
| onClear    | value: any   | Callback to invoke when input field is cleared.       |

## Templates

| Name      | Type              | Description                 |
| --------- | ----------------- | --------------------------- |
| clearicon | TemplateRef<void> | Custom clear icon template. |

**Full API & more examples:** https://primeng.org/inputmask
