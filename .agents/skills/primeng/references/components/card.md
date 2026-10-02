# Card (`p-card`)

Card is a flexible container component.

**Import:**

```ts
import { CardModule } from "primeng/card";
```

## Example

```typescript
import { Component } from "@angular/core";
import { CardModule } from "primeng/card";

@Component({
  template: `
    <div class="mb-4 p-8">
      <p-card header="Simple Card">
        <p class="m-0">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore
          sed consequuntur error repudiandae numquam deserunt quisquam repellat
          libero asperiores earum nam nobis, culpa ratione quam perferendis
          esse, cupiditate neque quas!
        </p>
      </p-card>
    </div>
  `,
  standalone: true,
  imports: [CardModule],
})
export class CardBasicDemo {}
```

## Inputs

| Name      | Type                     | Default | Description                  |
| --------- | ------------------------ | ------- | ---------------------------- |
| header    | string                   | -       | Header of the card.          |
| subheader | string                   | -       | Subheader of the card.       |
| style     | { [klass: string]: any } | -       | Inline style of the element. |

## Templates

| Name     | Type              | Description               |
| -------- | ----------------- | ------------------------- |
| header   | TemplateRef<void> | Custom header template.   |
| title    | TemplateRef<void> | Custom title template.    |
| subtitle | TemplateRef<void> | Custom subtitle template. |
| content  | TemplateRef<void> | Custom content template.  |
| footer   | TemplateRef<void> | Custom footer template.   |

**Full API & more examples:** https://primeng.org/card
