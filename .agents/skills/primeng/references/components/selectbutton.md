# SelectButton (`p-selectbutton`)

SelectButton is used to choose single or multiple items from a list using buttons.

**Import:**

```ts
import { SelectButtonModule } from "primeng/selectbutton";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { SelectButtonModule } from "primeng/selectbutton";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-selectbutton
        [options]="stateOptions"
        [(ngModel)]="value"
        optionLabel="label"
        optionValue="value"
        aria-labelledby="basic"
      />
    </div>
  `,
  standalone: true,
  imports: [SelectButtonModule, FormsModule],
})
export class SelectbuttonBasicDemo {
  stateOptions: any[];
  value: string = "one-way";
}
```

## Inputs

| Name           | Type                                       | Default   | Description                                                                                                     |
| -------------- | ------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------- |
| required       | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                                                 |
| invalid        | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.                                  |
| disabled       | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.                                 |
| name           | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                                          |
| options        | any[]                                      | -         | An array of selectitems to display as the available options.                                                    |
| optionLabel    | string                                     | -         | Name of the label field of an option.                                                                           |
| optionValue    | string                                     | -         | Name of the value field of an option.                                                                           |
| optionDisabled | string                                     | -         | Name of the disabled field of an option.                                                                        |
| unselectable   | boolean                                    | -         | Whether selection can be cleared.                                                                               |
| tabindex       | number                                     | 0         | Index of the element in tabbing order.                                                                          |
| multiple       | boolean                                    | false     | When specified, allows selecting multiple values.                                                               |
| allowEmpty     | boolean                                    | true      | Whether selection can not be cleared.                                                                           |
| styleClass     | string                                     | -         | Style class of the component.                                                                                   |
| ariaLabelledBy | string                                     | -         | Establishes relationships between the component and label(s) where its value should be one or more element IDs. |
| dataKey        | string                                     | -         | A property to uniquely identify a value in options.                                                             |
| autofocus      | boolean                                    | false     | When present, it specifies that the component should automatically get focus on load.                           |
| size           | InputSignal<"small" \| "large">            | undefined | Specifies the size of the component.                                                                            |
| fluid          | InputSignalWithTransform<boolean, unknown> | undefined | Spans 100% width of the container when enabled.                                                                 |

## Outputs

| Name          | Parameters                          | Description                             |
| ------------- | ----------------------------------- | --------------------------------------- |
| onOptionClick | event: SelectButtonOptionClickEvent | Callback to invoke on input click.      |
| onChange      | event: SelectButtonChangeEvent      | Callback to invoke on selection change. |

## Templates

| Name | Type                                         | Description           |
| ---- | -------------------------------------------- | --------------------- |
| item | TemplateRef<SelectButtonItemTemplateContext> | Custom item template. |

**Full API & more examples:** https://primeng.org/selectbutton
