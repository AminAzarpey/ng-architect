# Focus Trap (`pFocusTrap`)

Focus Trap keeps focus within a certain DOM element while tabbing.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { CheckboxModule } from "primeng/checkbox";
import { IconFieldModule } from "primeng/iconfield";
import { InputIconModule } from "primeng/inputicon";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { ButtonModule } from "primeng/button";
import { CheckboxModule } from "primeng/checkbox";
import { IconFieldModule } from "primeng/iconfield";
import { InputIconModule } from "primeng/inputicon";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <div pFocusTrap class="w-full sm:w-80 flex flex-col gap-6">
        <p-iconfield>
          <p-inputicon>
            <i class="pi pi-user"></i>
          </p-inputicon>
          <input
            type="text"
            pInputText
            id="input"
            [(ngModel)]="name"
            type="text"
            placeholder="Name"
            [pAutoFocus]="true"
            [fluid]="true"
          />
        </p-iconfield>
        <p-iconfield>
          <p-inputicon>
            <i class="pi pi-envelope"> </i>
          </p-inputicon>
          <input
            type="text"
            pInputText
            id="email"
            [(ngModel)]="email"
            type="email"
            placeholder="Email"
            [fluid]="true"
          />
        </p-iconfield>
        <div class="flex items-center gap-2">
          <p-checkbox
            id="accept"
            [(ngModel)]="accept"
            name="accept"
            value="Accept"
          />
          <label for="accept">I agree to the terms and conditions.</label>
        </div>
        <p-button
          type="submit"
          label="Submit"
          class="mt-2"
          styleClass="w-full"
        />
      </div>
    </div>
  `,
  standalone: true,
  imports: [
    ButtonModule,
    CheckboxModule,
    IconFieldModule,
    InputIconModule,
    InputTextModule,
    FormsModule,
  ],
})
export class FocustrapBasicDemo {
  name: string = "";
  email: string = "";
  accept: boolean = false;
}
```

## Inputs

| Name               | Type    | Default | Description                                  |
| ------------------ | ------- | ------- | -------------------------------------------- |
| pFocusTrapDisabled | boolean | false   | When set as true, focus wouldn't be managed. |

**Full API & more examples:** https://primeng.org/focustrap
