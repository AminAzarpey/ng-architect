# Checkbox (`p-checkbox`)

Checkbox is an extension to standard checkbox element with theming.

**Import:**

```ts
import { CheckboxModule } from "primeng/checkbox";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { CheckboxModule } from "primeng/checkbox";

@Component({
  template: `
    <div class="card flex justify-center gap-4">
      <p-checkbox [(ngModel)]="checked" [binary]="true" />
    </div>
  `,
  standalone: true,
  imports: [CheckboxModule, FormsModule],
})
export class CheckboxBasicDemo {
  checked: any = null;
}
```

## Inputs

| Name           | Type                                       | Default   | Description                                                                                                     |
| -------------- | ------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------- |
| required       | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                                                 |
| invalid        | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.                                  |
| disabled       | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.                                 |
| name           | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                                          |
| value          | any                                        | -         | Value of the checkbox.                                                                                          |
| binary         | boolean                                    | false     | Allows to select a boolean value instead of multiple values.                                                    |
| ariaLabelledBy | string                                     | -         | Establishes relationships between the component and label(s) where its value should be one or more element IDs. |
| ariaLabel      | string                                     | -         | Used to define a string that labels the input element.                                                          |
| tabindex       | number                                     | -         | Index of the element in tabbing order.                                                                          |
| inputId        | string                                     | -         | Identifier of the focus input to match a label defined for the component.                                       |
| inputStyle     | { [klass: string]: any }                   | -         | Inline style of the input element.                                                                              |
| inputClass     | string                                     | -         | Style class of the input element.                                                                               |
| indeterminate  | boolean                                    | false     | When present, it specifies input state as indeterminate.                                                        |
| formControl    | FormControl<any>                           | -         | Form control value.                                                                                             |
| checkboxIcon   | string                                     | -         | Icon class of the checkbox icon.                                                                                |
| readonly       | boolean                                    | false     | When present, it specifies that the component cannot be edited.                                                 |
| autofocus      | boolean                                    | false     | When present, it specifies that the component should automatically get focus on load.                           |
| trueValue      | any                                        | true      | Value in checked state.                                                                                         |
| falseValue     | any                                        | false     | Value in unchecked state.                                                                                       |
| variant        | InputSignal<"outlined" \| "filled">        | undefined | Specifies the input variant of the component.                                                                   |
| size           | InputSignal<"small" \| "large">            | undefined | Specifies the size of the component.                                                                            |

## Outputs

| Name     | Parameters                 | Description                                 |
| -------- | -------------------------- | ------------------------------------------- |
| onChange | event: CheckboxChangeEvent | Callback to invoke on value change.         |
| onFocus  | event: Event               | Callback to invoke when the receives focus. |
| onBlur   | event: Event               | Callback to invoke when the loses focus.    |

## Templates

| Name         | Type                                     | Description                    |
| ------------ | ---------------------------------------- | ------------------------------ |
| checkboxicon | TemplateRef<CheckboxIconTemplateContext> | Custom checkbox icon template. |

**Full API & more examples:** https://primeng.org/checkbox
