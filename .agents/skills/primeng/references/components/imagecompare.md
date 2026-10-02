# ImageCompare (`p-imagecompare`)

Compare two images side by side with a slider.

**Import:**

```ts
import { ImageCompareModule } from "primeng/imagecompare";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ImageCompareModule } from "primeng/imagecompare";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-imagecompare class="shadow-lg rounded-2xl">
        <ng-template #left>
          <img
            src="https://primefaces.org/cdn/primevue/images/compare/island1.jpg"
          />
        </ng-template>
        <ng-template #right>
          <img
            src="https://primefaces.org/cdn/primevue/images/compare/island2.jpg"
          />
        </ng-template>
      </p-imagecompare>
    </div>
  `,
  standalone: true,
  imports: [ImageCompareModule],
})
export class ImagecompareBasicDemo {}
```

**Full API & more examples:** https://primeng.org/imagecompare
