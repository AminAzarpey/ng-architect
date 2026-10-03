# InputGroup (`p-inputgroup`)

Text, icon, buttons and other content can be grouped next to an input.

**Import:**

```ts
import { SelectModule } from "primeng/select";
import { InputGroupModule } from "primeng/inputgroup";
import { InputNumberModule } from "primeng/inputnumber";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { SelectModule } from "primeng/select";
import { InputGroupModule } from "primeng/inputgroup";
import { InputNumberModule } from "primeng/inputnumber";
import { InputTextModule } from "primeng/inputtext";

interface City {
  name: string;
  code: string;
}

@Component({
  template: `
    <div class="card grid grid-cols-1 md:grid-cols-2 gap-4">
      <p-inputgroup>
        <p-inputgroup-addon>
          <i class="pi pi-user"></i>
        </p-inputgroup-addon>
        <input pInputText [(ngModel)]="text1" placeholder="Username" />
      </p-inputgroup>
      <p-inputgroup>
        <p-inputgroup-addon>$</p-inputgroup-addon>
        <p-inputnumber [(ngModel)]="number" placeholder="Price" />
        <p-inputgroup-addon>.00</p-inputgroup-addon>
      </p-inputgroup>
      <p-inputgroup>
        <p-inputgroup-addon>www</p-inputgroup-addon>
        <input pInputText [(ngModel)]="text2" placeholder="Website" />
      </p-inputgroup>
      <p-inputgroup>
        <p-inputgroup-addon>
          <i class="pi pi-map"></i>
        </p-inputgroup-addon>
        <p-select
          [(ngModel)]="selectedCity"
          [options]="cities"
          optionLabel="name"
          placeholder="City"
        />
      </p-inputgroup>
    </div>
  `,
  standalone: true,
  imports: [
    SelectModule,
    InputGroupModule,
    InputNumberModule,
    InputTextModule,
    FormsModule,
  ],
})
export class InputgroupBasicDemo {
  text1: string | undefined;
  text2: string | undefined;
  number: string | undefined;
  selectedCity: City | undefined;
  cities: City[];
}
```

**Full API & more examples:** https://primeng.org/inputgroup
