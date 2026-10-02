# Textarea (`pTextarea`)

Textarea adds styling and autoResize functionality to standard textarea element.

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";

@Component({
  template: `
    <div class="card flex justify-center">
      <textarea rows="5" cols="30" pTextarea [(ngModel)]="value"></textarea>
    </div>
  `,
  standalone: true,
  imports: [FormsModule],
})
export class TextareaBasicDemo {
  value!: string;
}
```

## Inputs

| Name              | Type                                       | Default   | Description                                                                    |
| ----------------- | ------------------------------------------ | --------- | ------------------------------------------------------------------------------ |
| pTextareaPT       | InputSignal<TextareaPassThrough>           | undefined | Used to pass attributes to DOM elements inside the Textarea component.         |
| pTextareaUnstyled | InputSignal<boolean>                       | undefined | Indicates whether the component should be rendered without styles.             |
| autoResize        | boolean                                    | false     | When present, textarea size changes as being typed.                            |
| pSize             | "small" \| "large"                         | -         | Defines the size of the component.                                             |
| variant           | InputSignal<"outlined" \| "filled">        | undefined | Specifies the input variant of the component.                                  |
| fluid             | InputSignalWithTransform<boolean, unknown> | undefined | Spans 100% width of the container when enabled.                                |
| invalid           | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style. |

## Outputs

| Name     | Parameters         | Description                            |
| -------- | ------------------ | -------------------------------------- |
| onResize | event: {} \| Event | Callback to invoke on textarea resize. |

**Full API & more examples:** https://primeng.org/textarea
