# MeterGroup (`p-metergroup`)

MeterGroup displays scalar measurements within a known range.

**Import:**

```ts
import { MeterGroupModule } from "primeng/metergroup";
```

## Example

```typescript
import { Component } from "@angular/core";
import { MeterGroupModule } from "primeng/metergroup";

@Component({
  template: `
    <div class="card">
      <p-metergroup [value]="value" />
    </div>
  `,
  standalone: true,
  imports: [MeterGroupModule],
})
export class MetergroupBasicDemo {
  value: any[] = [
    { label: "Space used", value: 15, color: "var(--p-primary-color)" },
  ];
}
```

**Full API & more examples:** https://primeng.org/metergroup
