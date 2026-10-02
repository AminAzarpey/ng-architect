# ProgressBar (`p-progressbar`)

ProgressBar is a process status indicator.

**Import:**

```ts
import { ProgressBarModule } from "primeng/progressbar";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ProgressBarModule } from "primeng/progressbar";

@Component({
  template: `
    <div class="card">
      <p-progressbar [value]="50" />
    </div>
  `,
  standalone: true,
  imports: [ProgressBarModule],
})
export class ProgressbarBasicDemo {}
```

## Inputs

| Name            | Type                             | Default       | Description                                |
| --------------- | -------------------------------- | ------------- | ------------------------------------------ |
| value           | number                           | -             | Current value of the progress.             |
| showValue       | boolean                          | true          | Whether to display the progress bar value. |
| valueStyleClass | string                           | -             | Style class of the value element.          |
| unit            | string                           | %             | Unit sign appended to the value.           |
| mode            | "indeterminate" \| "determinate" | 'determinate' | Defines the mode of the progress           |
| color           | string                           | -             | Color for the background of the progress.  |

## Templates

| Name    | Type                                           | Description              |
| ------- | ---------------------------------------------- | ------------------------ |
| content | TemplateRef<ProgressBarContentTemplateContext> | Template of the content. |

**Full API & more examples:** https://primeng.org/progressbar
