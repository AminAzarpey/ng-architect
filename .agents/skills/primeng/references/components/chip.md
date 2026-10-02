# Chip (`p-chip`)

Chip represents entities using icons, labels and images.

**Import:**

```ts
import { ChipModule } from "primeng/chip";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ChipModule } from "primeng/chip";

@Component({
  template: `
    <div class="card flex items-center gap-2 flex-wrap">
      <p-chip label="Action" />
      <p-chip label="Comedy" />
      <p-chip label="Mystery" />
      <p-chip label="Thriller" [removable]="true" />
    </div>
  `,
  standalone: true,
  imports: [ChipModule],
})
export class ChipBasicDemo {}
```

## Inputs

| Name       | Type      | Default | Description                                                         |
| ---------- | --------- | ------- | ------------------------------------------------------------------- |
| label      | string    | -       | Defines the text to display.                                        |
| icon       | string    | -       | Defines the icon to display.                                        |
| image      | string    | -       | Defines the image to display.                                       |
| alt        | string    | -       | Alt attribute of the image.                                         |
| disabled   | boolean   | false   | When present, it specifies that the element should be disabled.     |
| removable  | boolean   | false   | Whether to display a remove icon.                                   |
| removeIcon | string    | -       | Icon of the remove element.                                         |
| chipProps  | ChipProps | -       | Used to pass all properties of the chipProps to the Chip component. |

## Outputs

| Name         | Parameters        | Description                                                             |
| ------------ | ----------------- | ----------------------------------------------------------------------- |
| onRemove     | event: MouseEvent | Callback to invoke when a chip is removed.                              |
| onImageError | event: Event      | This event is triggered if an error occurs while loading an image file. |

## Templates

| Name       | Type              | Description                  |
| ---------- | ----------------- | ---------------------------- |
| removeicon | TemplateRef<void> | Custom remove icon template. |

**Full API & more examples:** https://primeng.org/chip
