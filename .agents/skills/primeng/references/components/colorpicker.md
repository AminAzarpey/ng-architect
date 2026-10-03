# ColorPicker (`p-colorpicker`)

ColorPicker is an input component to select a color.

**Import:**

```ts
import { ColorPickerModule } from "primeng/colorpicker";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { ColorPickerModule } from "primeng/colorpicker";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-colorpicker [(ngModel)]="color" />
    </div>
  `,
  standalone: true,
  imports: [ColorPickerModule, FormsModule],
})
export class ColorpickerBasicDemo {
  color: string | undefined;
}
```

## Inputs

| Name           | Type                                       | Default   | Description                                                                                                                                                                                                                                          |
| -------------- | ------------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required       | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                                                                                                                                                                                      |
| invalid        | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.                                                                                                                                                                       |
| disabled       | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.                                                                                                                                                                      |
| name           | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                                                                                                                                                                               |
| inline         | boolean                                    | false     | Whether to display as an overlay or not.                                                                                                                                                                                                             |
| format         | "rgb" \| "hex" \| "hsb"                    | hex       | Format to use in value binding.                                                                                                                                                                                                                      |
| tabindex       | string                                     | -         | Index of the element in tabbing order.                                                                                                                                                                                                               |
| inputId        | string                                     | -         | Identifier of the focus input to match a label defined for the dropdown.                                                                                                                                                                             |
| autoZIndex     | boolean                                    | true      | Whether to automatically manage layering.                                                                                                                                                                                                            |
| autofocus      | boolean                                    | false     | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                |
| defaultColor   | string                                     | ff0000    | Default color to display initially when model value is not present.                                                                                                                                                                                  |
| appendTo       | InputSignal<any>                           | 'self'    | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| overlayOptions | InputSignal<OverlayOptions>                | ...       | Whether to use overlay API feature. The properties of overlay API can be used like an object in it.                                                                                                                                                  |
| motionOptions  | InputSignal<MotionOptions>                 | ...       | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name     | Parameters                    | Description                            |
| -------- | ----------------------------- | -------------------------------------- |
| onChange | event: ColorPickerChangeEvent | Callback to invoke on value change.    |
| onShow   | value: any                    | Callback to invoke on panel is shown.  |
| onHide   | value: any                    | Callback to invoke on panel is hidden. |

**Full API & more examples:** https://primeng.org/colorpicker
