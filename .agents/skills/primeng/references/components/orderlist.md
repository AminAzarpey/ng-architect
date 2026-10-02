# OrderList (`p-orderlist`)

OrderList is used to sort a collection.

**Import:**

```ts
import { OrderListModule } from "primeng/orderlist";
```

## Example

```typescript
import { Component, OnInit, inject, signal } from "@angular/core";
import { OrderListModule } from "primeng/orderlist";
import { ProductService } from "@/service/productservice";
import { Product } from "@/domain/product";

@Component({
  template: `
    <div class="card sm:flex sm:justify-center">
      <p-orderlist
        [value]="products()"
        dataKey="id"
        [responsive]="true"
        breakpoint="575px"
      >
        <ng-template #item let-option>
          {{ option.name }}
        </ng-template>
      </p-orderlist>
    </div>
  `,
  standalone: true,
  imports: [OrderListModule],
  providers: [ProductService],
})
export class OrderlistBasicDemo implements OnInit {
  private productService = inject(ProductService);
  products = signal<Product[]>([]);

  ngOnInit() {
    this.productService.getProductsSmall().then((cars) => {
      this.products.set(cars);
    });
  }

  getSeverity(status: string) {
    switch (status) {
      case "INSTOCK":
        return "success";
      case "LOWSTOCK":
        return "warning";
      case "OUTOFSTOCK":
        return "danger";
    }
  }
}
```

## Inputs

| Name                  | Type                                                                                                          | Default  | Description                                                                                                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| header                | string                                                                                                        | -        | Text for the caption.                                                                                                                                                                                                 |
| tabindex              | number                                                                                                        | -        | Index of the element in tabbing order.                                                                                                                                                                                |
| ariaLabel             | string                                                                                                        | -        | Defines a string that labels the input for accessibility.                                                                                                                                                             |
| ariaLabelledBy        | string                                                                                                        | -        | Specifies one or more IDs in the DOM that labels the input field.                                                                                                                                                     |
| listStyle             | { [klass: string]: any }                                                                                      | -        | Inline style of the list element.                                                                                                                                                                                     |
| responsive            | boolean                                                                                                       | false    | A boolean value that indicates whether the component should be responsive.                                                                                                                                            |
| filterBy              | string                                                                                                        | -        | When specified displays an input field to filter the items on keyup and decides which fields to search against.                                                                                                       |
| filterPlaceholder     | string                                                                                                        | -        | Placeholder of the filter input.                                                                                                                                                                                      |
| filterLocale          | string                                                                                                        | -        | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                              |
| metaKeySelection      | boolean                                                                                                       | false    | When true metaKey needs to be pressed to select or unselect an item and when set to false selection of each item can be toggled individually. On touch enabled devices, metaKeySelection is turned off automatically. |
| dragdrop              | boolean                                                                                                       | false    | Whether to enable dragdrop based reordering.                                                                                                                                                                          |
| controlsPosition      | "right" \| "left"                                                                                             | left     | Defines the location of the buttons with respect to the list.                                                                                                                                                         |
| ariaFilterLabel       | string                                                                                                        | -        | Defines a string that labels the filter input.                                                                                                                                                                        |
| filterMatchMode       | "startsWith" \| "contains" \| "endsWith" \| "equals" \| "notEquals" \| "in" \| "lt" \| "lte" \| "gt" \| "gte" | contains | Defines how the items are filtered.                                                                                                                                                                                   |
| breakpoint            | string                                                                                                        | 960px    | Indicates the width of the screen at which the component should change its behavior.                                                                                                                                  |
| stripedRows           | boolean                                                                                                       | false    | Whether to displays rows with alternating colors.                                                                                                                                                                     |
| disabled              | boolean                                                                                                       | false    | When present, it specifies that the component should be disabled.                                                                                                                                                     |
| trackBy               | Function                                                                                                      | ...      | Function to optimize the dom operations by delegating to ngForTrackBy, default algorithm checks for object identity.                                                                                                  |
| scrollHeight          | string                                                                                                        | 14rem    | Height of the viewport, a scrollbar is defined if height of list exceeds this value.                                                                                                                                  |
| autoOptionFocus       | boolean                                                                                                       | true     | Whether to focus on the first visible or selected element.                                                                                                                                                            |
| dataKey               | string                                                                                                        | -        | Name of the field that uniquely identifies the record in the data.                                                                                                                                                    |
| selection             | any[]                                                                                                         | -        | A list of values that are currently selected.                                                                                                                                                                         |
| value                 | any[]                                                                                                         | -        | Array of values to be displayed in the component. It represents the data source for the list of items.                                                                                                                |
| buttonProps           | ButtonProps                                                                                                   | ...      | Used to pass all properties of the ButtonProps to the Button component.                                                                                                                                               |
| moveUpButtonProps     | ButtonProps                                                                                                   | -        | Used to pass all properties of the ButtonProps to the move up button inside the component.                                                                                                                            |
| moveTopButtonProps    | ButtonProps                                                                                                   | -        | Used to pass all properties of the ButtonProps to the move top button inside the component.                                                                                                                           |
| moveDownButtonProps   | ButtonProps                                                                                                   | -        | Used to pass all properties of the ButtonProps to the move down button inside the component.                                                                                                                          |
| moveBottomButtonProps | ButtonProps                                                                                                   | -        | Used to pass all properties of the ButtonProps to the move bottom button inside the component.                                                                                                                        |

## Outputs

| Name              | Parameters                           | Description                                 |
| ----------------- | ------------------------------------ | ------------------------------------------- |
| selectionChange   | value: any                           | Callback to invoke on selection change.     |
| onReorder         | value: any                           | Callback to invoke when list is reordered.  |
| onSelectionChange | event: OrderListSelectionChangeEvent | Callback to invoke when selection changes.  |
| onFilterEvent     | event: OrderListFilterEvent          | Callback to invoke when filtering occurs.   |
| onFocus           | event: Event                         | Callback to invoke when the list is focused |
| onBlur            | event: Event                         | Callback to invoke when the list is blurred |

## Templates

| Name               | Type                                        | Description                       |
| ------------------ | ------------------------------------------- | --------------------------------- |
| item               | TemplateRef<OrderListItemTemplateContext>   | Custom item template.             |
| emptymessage       | TemplateRef<void>                           | Custom empty template.            |
| emptyfiltermessage | TemplateRef<void>                           | Custom empty filter template.     |
| filter             | TemplateRef<OrderListFilterTemplateContext> | Custom filter template.           |
| header             | TemplateRef<void>                           | Custom header template.           |
| moveupicon         | TemplateRef<void>                           | Custom move up icon template.     |
| movetopicon        | TemplateRef<void>                           | Custom move top icon template.    |
| movedownicon       | TemplateRef<void>                           | Custom move down icon template.   |
| movebottomicon     | TemplateRef<void>                           | Custom move bottom icon template. |
| filtericon         | TemplateRef<void>                           | Custom filter icon template.      |

## Methods

| Name        | Parameters | Return Type | Description                         |
| ----------- | ---------- | ----------- | ----------------------------------- |
| resetFilter |            | void        | Callback to invoke on filter reset. |

**Full API & more examples:** https://primeng.org/orderlist
