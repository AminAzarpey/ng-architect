# Tag (`p-tag`)

Tag component is used to categorize content.

**Import:**

```ts
import { TagModule } from "primeng/tag";
```

## Example

```typescript
import { Component } from "@angular/core";
import { TagModule } from "primeng/tag";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-tag value="New" />
    </div>
  `,
  standalone: true,
  imports: [TagModule],
})
export class TagBasicDemo {}
```

## Inputs

| Name     | Type                                                                   | Default | Description                                   |
| -------- | ---------------------------------------------------------------------- | ------- | --------------------------------------------- |
| severity | "success" \| "info" \| "warn" \| "danger" \| "secondary" \| "contrast" | -       | Severity type of the tag.                     |
| value    | string                                                                 | -       | Value to display inside the tag.              |
| icon     | string                                                                 | -       | Icon of the tag to display next to the value. |
| rounded  | boolean                                                                | false   | Whether the corners of the tag are rounded.   |

## Templates

| Name | Type              | Description           |
| ---- | ----------------- | --------------------- |
| icon | TemplateRef<void> | Custom icon template. |

**Full API & more examples:** https://primeng.org/tag
