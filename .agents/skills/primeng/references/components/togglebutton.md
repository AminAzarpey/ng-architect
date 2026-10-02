# ToggleButton (`p-togglebutton`)

ToggleButton is used to select a boolean value using a button.

**Import:**

```ts
import { ToggleButtonModule } from "primeng/togglebutton";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { ToggleButtonModule } from "primeng/togglebutton";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-togglebutton
        [(ngModel)]="checked"
        onLabel="On"
        offLabel="Off"
        class="w-24"
      />
    </div>
  `,
  standalone: true,
  imports: [ToggleButtonModule, FormsModule],
})
export class TogglebuttonBasicDemo {
  checked: boolean = false;
}
```

## Inputs

| Name           | Type                                       | Default   | Description                                                                                                     |
| -------------- | ------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------- |
| required       | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                                                 |
| invalid        | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.                                  |
| disabled       | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.                                 |
| name           | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                                          |
| onLabel        | string                                     | Yes       | Label for the on state.                                                                                         |
| offLabel       | string                                     | No        | Label for the off state.                                                                                        |
| onIcon         | string                                     | -         | Icon for the on state.                                                                                          |
| offIcon        | string                                     | -         | Icon for the off state.                                                                                         |
| ariaLabel      | string                                     | -         | Defines a string that labels the input for accessibility.                                                       |
| ariaLabelledBy | string                                     | -         | Establishes relationships between the component and label(s) where its value should be one or more element IDs. |
| inputId        | string                                     | -         | Identifier of the focus input to match a label defined for the component.                                       |
| tabindex       | number                                     | 0         | Index of the element in tabbing order.                                                                          |
| iconPos        | "right" \| "left"                          | left      | Position of the icon.                                                                                           |
| autofocus      | boolean                                    | false     | When present, it specifies that the component should automatically get focus on load.                           |
| size           | "small" \| "large"                         | -         | Defines the size of the component.                                                                              |
| allowEmpty     | boolean                                    | false     | Whether selection can not be cleared.                                                                           |
| fluid          | InputSignalWithTransform<boolean, unknown> | undefined | Spans 100% width of the container when enabled.                                                                 |

## Outputs

| Name     | Parameters                     | Description                         |
| -------- | ------------------------------ | ----------------------------------- |
| onChange | event: ToggleButtonChangeEvent | Callback to invoke on value change. |

## Templates

| Name    | Type                                            | Description              |
| ------- | ----------------------------------------------- | ------------------------ |
| icon    | TemplateRef<ToggleButtonIconTemplateContext>    | Custom icon template.    |
| content | TemplateRef<ToggleButtonContentTemplateContext> | Custom content template. |

**Full API & more examples:** https://primeng.org/togglebutton
