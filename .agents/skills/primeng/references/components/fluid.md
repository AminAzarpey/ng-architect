# Fluid (`p-fluid`)

Fluid is a layout component to make descendant components span full width of their container.

**Import:**

```ts
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex flex-col gap-6">
      <div>
        <label for="non-fluid" class="font-bold mb-2 block">Non-Fluid</label>
        <input type="text" pInputText id="non-fluid" />
      </div>
      <div>
        <label for="fluid" class="font-bold mb-2 block">Fluid Prop</label>
        <input type="text" pInputText id="fluid" fluid />
      </div>
      <p-fluid>
        <span class="font-bold mb-2 block">Fluid Container</span>
        <div class="grid grid-cols-2 gap-4">
          <div><input type="text" pInputText /></div>
          <div><input type="text" pInputText /></div>
          <div class="col-span-full"><input type="text" pInputText /></div>
          <div>
            <input
              type="text"
              pInputText
              [fluid]="false"
              placeholder="Non-Fluid"
            />
          </div>
        </div>
      </p-fluid>
    </div>
  `,
  standalone: true,
  imports: [InputTextModule],
})
export class FluidBasicDemo {}
```

**Full API & more examples:** https://primeng.org/fluid
