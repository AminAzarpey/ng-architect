# Password (`p-password`)

Password displays strength indicator for password fields.

**Import:**

```ts
import { PasswordModule } from "primeng/password";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { PasswordModule } from "primeng/password";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-password [(ngModel)]="value" [feedback]="false" autocomplete="off" />
    </div>
  `,
  standalone: true,
  imports: [PasswordModule, FormsModule],
})
export class PasswordBasicDemo {
  value!: string;
}
```

## Inputs

| Name            | Type                                       | Default                                      | Description                                                                                                                                                                                                                                          |
| --------------- | ------------------------------------------ | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------- |
| required        | InputSignalWithTransform<boolean, unknown> | false                                        | There must be a value (if set).                                                                                                                                                                                                                      |
| invalid         | InputSignalWithTransform<boolean, unknown> | false                                        | When present, it specifies that the component should have invalid state style.                                                                                                                                                                       |
| disabled        | InputSignalWithTransform<boolean, unknown> | false                                        | When present, it specifies that the component should have disabled state style.                                                                                                                                                                      |
| name            | InputSignal<string>                        | undefined                                    | When present, it specifies that the name of the input.                                                                                                                                                                                               |
| fluid           | InputSignalWithTransform<boolean, unknown> | false                                        | Spans 100% width of the container when enabled.                                                                                                                                                                                                      |
| variant         | InputSignal<"outlined" \| "filled">        | 'outlined'                                   | Specifies the input variant of the component.                                                                                                                                                                                                        |
| size            | InputSignal<"small" \| "large">            | undefined                                    | Specifies the size of the component.                                                                                                                                                                                                                 |
| inputSize       | InputSignal<number>                        | undefined                                    | Specifies the visible width of the input element in characters.                                                                                                                                                                                      |
| pattern         | InputSignal<string>                        | undefined                                    | Specifies the value must match the pattern.                                                                                                                                                                                                          |
| min             | InputSignal<number>                        | undefined                                    | The value must be greater than or equal to the value.                                                                                                                                                                                                |
| max             | InputSignal<number>                        | undefined                                    | The value must be less than or equal to the value.                                                                                                                                                                                                   |
| step            | InputSignal<number>                        | undefined                                    | Unless the step is set to the any literal, the value must be min + an integral multiple of the step.                                                                                                                                                 |
| minlength       | InputSignal<number>                        | undefined                                    | The number of characters (code points) must not be less than the value of the attribute, if non-empty.                                                                                                                                               |
| maxlength       | InputSignal<number>                        | undefined                                    | The number of characters (code points) must not exceed the value of the attribute.                                                                                                                                                                   |
| ariaLabel       | string                                     | -                                            | Defines a string that labels the input for accessibility.                                                                                                                                                                                            |
| ariaLabelledBy  | string                                     | -                                            | Specifies one or more IDs in the DOM that labels the input field.                                                                                                                                                                                    |
| label           | string                                     | -                                            | Label of the input for accessibility.                                                                                                                                                                                                                |
| promptLabel     | string                                     | -                                            | Text to prompt password entry. Defaults to PrimeNG I18N API configuration.                                                                                                                                                                           |
| mediumRegex     | string                                     | ^(((?=._[a-z])(?=._[A-Z]))                   | ((?=._[a-z])(?=._[0-9]))                                                                                                                                                                                                                             | ((?=._[A-Z])(?=._[0-9])))(?=.{6,}) | Regex value for medium regex. |
| strongRegex     | string                                     | ^(?=._[a-z])(?=._[A-Z])(?=.\*[0-9])(?=.{8,}) | Regex value for strong regex.                                                                                                                                                                                                                        |
| weakLabel       | string                                     | -                                            | Text for a weak password. Defaults to PrimeNG I18N API configuration.                                                                                                                                                                                |
| mediumLabel     | string                                     | -                                            | Text for a medium password. Defaults to PrimeNG I18N API configuration.                                                                                                                                                                              |
| strongLabel     | string                                     | -                                            | Text for a strong password. Defaults to PrimeNG I18N API configuration.                                                                                                                                                                              |
| inputId         | string                                     | -                                            | Identifier of the accessible input element.                                                                                                                                                                                                          |
| feedback        | boolean                                    | true                                         | Whether to show the strength indicator or not.                                                                                                                                                                                                       |
| toggleMask      | boolean                                    | false                                        | Whether to show an icon to display the password as plain text.                                                                                                                                                                                       |
| inputStyleClass | string                                     | -                                            | Style class of the input field.                                                                                                                                                                                                                      |
| inputStyle      | { [klass: string]: any }                   | -                                            | Inline style of the input field.                                                                                                                                                                                                                     |
| autocomplete    | string                                     | -                                            | Specify automated assistance in filling out password by browser.                                                                                                                                                                                     |
| placeholder     | string                                     | -                                            | Advisory information to display on input.                                                                                                                                                                                                            |
| showClear       | boolean                                    | false                                        | When enabled, a clear icon is displayed to clear the value.                                                                                                                                                                                          |
| autofocus       | boolean                                    | false                                        | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                |
| tabindex        | number                                     | -                                            | Index of the element in tabbing order.                                                                                                                                                                                                               |
| appendTo        | InputSignal<any>                           | 'self'                                       | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions   | InputSignal<MotionOptions>                 | ...                                          | The motion options.                                                                                                                                                                                                                                  |
| overlayOptions  | OverlayOptions                             | -                                            | Whether to use overlay API feature. The properties of overlay API can be used like an object in it.                                                                                                                                                  |

## Outputs

| Name    | Parameters   | Description                                           |
| ------- | ------------ | ----------------------------------------------------- |
| onFocus | event: Event | Callback to invoke when the component receives focus. |
| onBlur  | event: Event | Callback to invoke when the component loses focus.    |
| onClear | value: any   | Callback to invoke when clear button is clicked.      |

## Templates

| Name      | Type                                     | Description                    |
| --------- | ---------------------------------------- | ------------------------------ |
| content   | TemplateRef<void>                        | Custom template of content.    |
| footer    | TemplateRef<void>                        | Custom template of footer.     |
| header    | TemplateRef<void>                        | Custom template of header.     |
| clearicon | TemplateRef<void>                        | Custom template of clear icon. |
| hideicon  | TemplateRef<PasswordIconTemplateContext> | Custom template of hide icon.  |
| showicon  | TemplateRef<PasswordIconTemplateContext> | Custom template of show icon.  |

**Full API & more examples:** https://primeng.org/password
