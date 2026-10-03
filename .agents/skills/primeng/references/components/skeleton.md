# Skeleton (`p-skeleton`)

Skeleton is a placeholder to display instead of the actual content.

**Import:**

```ts
import { SkeletonModule } from "primeng/skeleton";
```

## Example

```typescript
import { Component } from "@angular/core";
import { SkeletonModule } from "primeng/skeleton";

@Component({
  template: `
    <div class="card">
      <div
        class="rounded border border-surface-200 dark:border-surface-700 p-6 bg-surface-0 dark:bg-surface-900"
      >
        <div class="flex mb-4">
          <p-skeleton shape="circle" size="4rem" class="mr-2" />
          <div>
            <p-skeleton width="10rem" class="mb-2" />
            <p-skeleton width="5rem" class="mb-2" />
            <p-skeleton height=".5rem" />
          </div>
        </div>
        <p-skeleton width="100%" height="150px" />
        <div class="flex justify-between mt-4">
          <p-skeleton width="4rem" height="2rem" />
          <p-skeleton width="4rem" height="2rem" />
        </div>
      </div>
    </div>
  `,
  standalone: true,
  imports: [SkeletonModule],
})
export class SkeletonCardDemo {}
```

## Inputs

| Name         | Type   | Default   | Description                                                 |
| ------------ | ------ | --------- | ----------------------------------------------------------- |
| shape        | string | rectangle | Shape of the element.                                       |
| borderRadius | string | -         | Border radius of the element, defaults to value from theme. |
| size         | string | -         | Size of the skeleton.                                       |
| width        | string | 100%      | Width of the element.                                       |
| height       | string | 1rem      | Height of the element.                                      |

**Full API & more examples:** https://primeng.org/skeleton
