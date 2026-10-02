# Ripple (`pRipple`)

Ripple directive adds ripple effect to the host element.

**Import:**

```ts
import { RippleModule } from "primeng/ripple";
```

## Example

```typescript
import { Component } from "@angular/core";
import { RippleModule } from "primeng/ripple";

@Component({
  template: `
    <div class="card flex flex-col gap-4 items-center">
      <span
        >Ripple option at the
        <span
          class="mx-1 h-8 w-8 rounded-border inline-flex items-center justify-center bg-primary text-primary-contrast"
          ><i class="pi pi-palette"></i
        ></span>
        configurator needs to be turned on for the demo.</span
      >
      <div class="flex justify-center gap-2">
        <div
          pRipple
          class="box"
          style="border: 1px solid rgba(75, 175, 80, 0.3); --p-ripple-background: rgba(75, 175, 80, 0.3)"
        >
          Green
        </div>
        <div
          pRipple
          class="box"
          style="border: 1px solid rgba(255, 193, 6, 0.3); --p-ripple-background: rgba(255, 193, 6, 0.3)"
        >
          Orange
        </div>
        <div
          pRipple
          class="box"
          style="border: 1px solid rgba(156, 39, 176, 0.3); --p-ripple-background: rgba(156, 39, 176, 0.3)"
        >
          Purple
        </div>
      </div>
    </div>
  `,
  standalone: true,
  imports: [RippleModule],
})
export class RippleCustomDemo {}
```

**Full API & more examples:** https://primeng.org/ripple
