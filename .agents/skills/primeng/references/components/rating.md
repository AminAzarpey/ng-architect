# Rating (`p-rating`)

Rating component is a star based selection input.

**Import:**

```ts
import { RatingModule } from "primeng/rating";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { RatingModule } from "primeng/rating";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-rating [(ngModel)]="value" />
    </div>
  `,
  standalone: true,
  imports: [RatingModule, FormsModule],
})
export class RatingBasicDemo {
  value!: number;
}
```

## Inputs

| Name         | Type                                       | Default   | Description                                                                           |
| ------------ | ------------------------------------------ | --------- | ------------------------------------------------------------------------------------- |
| required     | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                       |
| invalid      | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.        |
| disabled     | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.       |
| name         | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                |
| readonly     | boolean                                    | false     | When present, changing the value is not possible.                                     |
| stars        | number                                     | 5         | Number of stars.                                                                      |
| iconOnClass  | string                                     | -         | Style class of the on icon.                                                           |
| iconOnStyle  | { [klass: string]: any }                   | -         | Inline style of the on icon.                                                          |
| iconOffClass | string                                     | -         | Style class of the off icon.                                                          |
| iconOffStyle | { [klass: string]: any }                   | -         | Inline style of the off icon.                                                         |
| autofocus    | boolean                                    | false     | When present, it specifies that the component should automatically get focus on load. |

## Outputs

| Name    | Parameters             | Description                             |
| ------- | ---------------------- | --------------------------------------- |
| onRate  | event: RatingRateEvent | Emitted on value change.                |
| onFocus | event: FocusEvent      | Emitted when the rating receives focus. |
| onBlur  | event: FocusEvent      | Emitted when the rating loses focus.    |

## Templates

| Name    | Type                                   | Description               |
| ------- | -------------------------------------- | ------------------------- |
| onicon  | TemplateRef<RatingIconTemplateContext> | Custom on icon template.  |
| officon | TemplateRef<RatingIconTemplateContext> | Custom off icon template. |

**Full API & more examples:** https://primeng.org/rating
