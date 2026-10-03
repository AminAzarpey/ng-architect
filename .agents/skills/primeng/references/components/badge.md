# Badge (`p-badge`)

Badge is a small status indicator for another element.

**Import:**

```ts
import { BadgeModule } from "primeng/badge";
```

## Example

```typescript
import { Component } from "@angular/core";
import { BadgeModule } from "primeng/badge";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-badge value="2" />
    </div>
  `,
  standalone: true,
  imports: [BadgeModule],
})
export class BadgeBasicDemo {}
```

## Inputs

| Name          | Type                                                                                | Default | Description                                                |
| ------------- | ----------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------- |
| badgeSize     | InputSignal<"small" \| "large" \| "xlarge">                                         | ...     | Size of the badge, valid options are "large" and "xlarge". |
| size          | InputSignal<"small" \| "large" \| "xlarge">                                         | ...     | Size of the badge, valid options are "large" and "xlarge". |
| severity      | InputSignal<"success" \| "info" \| "warn" \| "danger" \| "secondary" \| "contrast"> | ...     | Severity type of the badge.                                |
| value         | InputSignal<string \| number>                                                       | ...     | Value to display inside the badge.                         |
| badgeDisabled | InputSignalWithTransform<boolean, boolean>                                          | ...     | When specified, disables the component.                    |

**Full API & more examples:** https://primeng.org/badge
