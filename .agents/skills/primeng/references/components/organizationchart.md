# Organization Chart

OrganizationChart visualizes hierarchical organization data.

**Import:**

```ts
import { TreeNode } from "primeng/api";
```

## Example

```typescript
import { Component } from "@angular/core";
import { TreeNode } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center overflow-x-auto">
      <p-organization-chart [value]="data" />
    </div>
  `,
  standalone: true,
  imports: [],
})
export class OrganizationchartBasicDemo {
  data: TreeNode[];
}
```

**Full API & more examples:** https://primeng.org/organizationchart
