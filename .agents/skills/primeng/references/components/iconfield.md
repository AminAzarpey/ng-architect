# IconField (`p-iconfield`)

IconField wraps an input and an icon.

**Import:**

```ts
import { IconFieldModule } from "primeng/iconfield";
import { InputIconModule } from "primeng/inputicon";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { IconFieldModule } from "primeng/iconfield";
import { InputIconModule } from "primeng/inputicon";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex flex-wrap justify-center gap-4">
      <p-iconfield>
        <p-inputicon class="pi pi-search" />
        <input type="text" pInputText placeholder="Search" />
      </p-iconfield>
      <p-iconfield>
        <input type="text" pInputText />
        <p-inputicon class="pi pi-spinner pi-spin" />
      </p-iconfield>
    </div>
  `,
  standalone: true,
  imports: [IconFieldModule, InputIconModule, InputTextModule],
})
export class IconfieldBasicDemo {}
```

## Inputs

| Name         | Type              | Default | Description           |
| ------------ | ----------------- | ------- | --------------------- |
| iconPosition | "right" \| "left" | left    | Position of the icon. |

**Full API & more examples:** https://primeng.org/iconfield
