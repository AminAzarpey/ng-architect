# ProgressSpinner

ProgressSpinner is a process status indicator.

## Example

```typescript
import { Component } from "@angular/core";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-progress-spinner ariaLabel="loading" />
    </div>
  `,
  standalone: true,
  imports: [],
})
export class ProgressspinnerBasicDemo {}
```

## Inputs

| Name              | Type   | Default | Description                                                |
| ----------------- | ------ | ------- | ---------------------------------------------------------- |
| strokeWidth       | string | 2       | Width of the circle stroke.                                |
| fill              | string | none    | Color for the background of the circle.                    |
| animationDuration | string | 2s      | Duration of the rotate animation.                          |
| ariaLabel         | string | -       | Used to define a aria label attribute the current element. |

**Full API & more examples:** https://primeng.org/progressspinner
