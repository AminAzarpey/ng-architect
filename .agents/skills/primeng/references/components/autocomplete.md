# AutoComplete (`p-autocomplete`)

AutoComplete is an input component that provides real-time suggestions when being typed.

**Import:**

```ts
import { AutoCompleteModule } from "primeng/autocomplete";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { AutoCompleteModule } from "primeng/autocomplete";

interface AutoCompleteCompleteEvent {
  originalEvent: Event;
  query: string;
}

@Component({
  template: `
    <div class="card flex justify-center">
      <p-autocomplete
        [(ngModel)]="value"
        [suggestions]="items"
        (completeMethod)="search($event)"
      />
    </div>
  `,
  standalone: true,
  imports: [AutoCompleteModule, FormsModule],
})
export class AutocompleteBasicDemo {
  items: any[] = [];
  value: any;

  search(event: AutoCompleteCompleteEvent) {
    this.items = [...Array(10).keys()].map((item) => event.query + "-" + item);
  }
}
```

**Full API & more examples:** https://primeng.org/autocomplete
