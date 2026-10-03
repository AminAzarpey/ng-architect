# Slider (`p-slider`)

Slider is a component to provide input with a drag handle.

**Import:**

```ts
import { SliderModule } from "primeng/slider";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { SliderModule } from "primeng/slider";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-slider [(ngModel)]="value" class="w-56" />
    </div>
  `,
  standalone: true,
  imports: [SliderModule, FormsModule],
})
export class SliderBasicDemo {
  value!: number;
}
```

## Inputs

| Name           | Type                                       | Default    | Description                                                                                                     |
| -------------- | ------------------------------------------ | ---------- | --------------------------------------------------------------------------------------------------------------- |
| required       | InputSignalWithTransform<boolean, unknown> | false      | There must be a value (if set).                                                                                 |
| invalid        | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have invalid state style.                                  |
| disabled       | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have disabled state style.                                 |
| name           | InputSignal<string>                        | undefined  | When present, it specifies that the name of the input.                                                          |
| animate        | boolean                                    | false      | When enabled, displays an animation on click of the slider bar.                                                 |
| min            | number                                     | 0          | Mininum boundary value.                                                                                         |
| max            | number                                     | 100        | Maximum boundary value.                                                                                         |
| orientation    | "vertical" \| "horizontal"                 | horizontal | Orientation of the slider.                                                                                      |
| step           | number                                     | -          | Step factor to increment/decrement the value.                                                                   |
| range          | boolean                                    | false      | When specified, allows two boundary values to be picked.                                                        |
| ariaLabel      | string                                     | -          | Defines a string that labels the input for accessibility.                                                       |
| ariaLabelledBy | string                                     | -          | Establishes relationships between the component and label(s) where its value should be one or more element IDs. |
| tabindex       | number                                     | 0          | Index of the element in tabbing order.                                                                          |
| autofocus      | boolean                                    | false      | When present, it specifies that the component should automatically get focus on load.                           |

## Outputs

| Name       | Parameters                 | Description                          |
| ---------- | -------------------------- | ------------------------------------ |
| onChange   | event: SliderChangeEvent   | Callback to invoke on value change.  |
| onSlideEnd | event: SliderSlideEndEvent | Callback to invoke when slide ended. |

**Full API & more examples:** https://primeng.org/slider
