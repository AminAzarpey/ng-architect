# Knob (`p-knob`)

Knob is a form component to define number inputs with a dial.

**Import:**

```ts
import { KnobModule } from "primeng/knob";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { KnobModule } from "primeng/knob";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-knob [(ngModel)]="value" />
    </div>
  `,
  standalone: true,
  imports: [KnobModule, FormsModule],
})
export class KnobBasicDemo {
  value!: number;
}
```

## Inputs

| Name           | Type                                       | Default   | Description                                                                     |
| -------------- | ------------------------------------------ | --------- | ------------------------------------------------------------------------------- |
| required       | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                 |
| invalid        | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.  |
| disabled       | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style. |
| name           | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                          |
| ariaLabel      | string                                     | -         | Defines a string that labels the input for accessibility.                       |
| ariaLabelledBy | string                                     | -         | Specifies one or more IDs in the DOM that labels the input field.               |
| tabindex       | number                                     | 0         | Index of the element in tabbing order.                                          |
| valueColor     | string                                     | ...       | Background of the value.                                                        |
| rangeColor     | string                                     | ...       | Background color of the range.                                                  |
| textColor      | string                                     | ...       | Color of the value text.                                                        |
| valueTemplate  | string                                     | {value}   | Template string of the value.                                                   |
| size           | number                                     | 100       | Size of the component in pixels.                                                |
| min            | number                                     | 0         | Mininum boundary value.                                                         |
| max            | number                                     | 100       | Maximum boundary value.                                                         |
| step           | number                                     | 1         | Step factor to increment/decrement the value.                                   |
| strokeWidth    | number                                     | 14        | Width of the knob stroke.                                                       |
| showValue      | boolean                                    | true      | Whether the show the value inside the knob.                                     |
| readonly       | boolean                                    | false     | When present, it specifies that the component value cannot be edited.           |

## Outputs

| Name     | Parameters    | Description                         |
| -------- | ------------- | ----------------------------------- |
| onChange | value: number | Callback to invoke on value change. |

**Full API & more examples:** https://primeng.org/knob
