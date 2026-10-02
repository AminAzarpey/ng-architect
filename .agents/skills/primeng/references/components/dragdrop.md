# Drag and Drop (`pDraggable / pDroppable`)

pDraggable and pDroppable directives apply drag-drop behaviors to any element.

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { Product } from "@/domain/product";

@Component({
  template: `
    <div class="card flex flex-wrap gap-4">
      <div class="p-2 border border-surface rounded-border w-60">
        <ul class="list-none flex flex-col gap-2 p-0 m-0">
          <li
            *ngFor="let product of availableProducts"
            class="p-2 rounded-border shadow-sm"
            pDraggable
            (onDragStart)="dragStart(product)"
            (onDragEnd)="dragEnd()"
          >
            {{ product.name }}
          </li>
        </ul>
      </div>
      <div
        class="p-2 border border-surface rounded-border w-60"
        pDroppable
        (onDrop)="drop()"
      >
        <p class="text-center border-surface border-b">Drop Zone</p>
        <ul
          class="list-none flex flex-col gap-2 p-0 m-0"
          *ngIf="selectedProducts"
        >
          <li
            *ngFor="let product of selectedProducts"
            class="p-2 rounded-border shadow-sm"
          >
            {{ product.name }}
          </li>
        </ul>
      </div>
    </div>
  `,
  standalone: true,
  imports: [],
})
export class DragdropBasicDemo implements OnInit {
  availableProducts: Product[] | undefined;
  selectedProducts: Product[] | undefined;
  draggedProduct: Product | undefined | null;

  ngOnInit() {
    this.selectedProducts = [];
    this.availableProducts = [
      { id: "1", name: "Black Watch" },
      { id: "2", name: "Bamboo Watch" },
    ];
  }

  dragStart(product: Product) {
    this.draggedProduct = product;
  }

  drop() {
    if (this.draggedProduct) {
      let draggedProductIndex = this.findIndex(this.draggedProduct);
      this.selectedProducts = [
        ...(this.selectedProducts as Product[]),
        this.draggedProduct,
      ];
      this.availableProducts = this.availableProducts?.filter(
        (val, i) => i != draggedProductIndex,
      );
      this.draggedProduct = null;
    }
  }

  dragEnd() {
    this.draggedProduct = null;
  }

  findIndex(product: Product) {
    let index = -1;
    for (let i = 0; i < (this.availableProducts as Product[]).length; i++) {
      if (product.id === (this.availableProducts as Product[])[i].id) {
        index = i;
        break;
      }
    }
    return index;
  }
}
```

**Full API & more examples:** https://primeng.org/dragdrop
