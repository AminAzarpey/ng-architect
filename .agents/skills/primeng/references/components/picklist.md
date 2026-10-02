# PickList (`p-picklist`)

PickList is used to reorder items between different lists.

**Import:**

```ts
import { PickListModule } from "primeng/picklist";
```

## Example

```typescript
import { Component, OnInit, inject, signal } from "@angular/core";
import { PickListModule } from "primeng/picklist";
import { ProductService } from "@/service/productservice";
import { Product } from "@/domain/product";

@Component({
  template: `
    <div class="card">
      <p-picklist
        [source]="sourceProducts()"
        [target]="targetProducts()"
        [dragdrop]="true"
        [responsive]="true"
        breakpoint="1400px"
      >
        <ng-template let-item #item>
          {{ item.name }}
        </ng-template>
      </p-picklist>
    </div>
  `,
  standalone: true,
  imports: [PickListModule],
  providers: [ProductService],
})
export class PicklistBasicDemo implements OnInit {
  private productService = inject(ProductService);
  sourceProducts = signal<Product[]>([]);
  targetProducts = signal<Product[]>([]);

  ngOnInit() {
    this.carService.getProductsSmall().then((products) => {
      this.sourceProducts.set(products);
    });
  }
}
```

## Inputs

| Name                    | Type                               | Default  | Description                                                                                                                                                                                                                                                       |
| ----------------------- | ---------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source                  | ModelSignal<any[]>                 | ...      | An array of objects for the source list.                                                                                                                                                                                                                          |
| target                  | ModelSignal<any[]>                 | ...      | An array of objects for the target list.                                                                                                                                                                                                                          |
| dataKey                 | string                             | -        | Name of the field that uniquely identifies the options.                                                                                                                                                                                                           |
| sourceHeader            | string                             | -        | Text for the source list caption                                                                                                                                                                                                                                  |
| tabindex                | number                             | 0        | Index of the element in tabbing order.                                                                                                                                                                                                                            |
| rightButtonAriaLabel    | string                             | -        | Defines a string that labels the move to right button for accessibility.                                                                                                                                                                                          |
| leftButtonAriaLabel     | string                             | -        | Defines a string that labels the move to left button for accessibility.                                                                                                                                                                                           |
| allRightButtonAriaLabel | string                             | -        | Defines a string that labels the move to all right button for accessibility.                                                                                                                                                                                      |
| allLeftButtonAriaLabel  | string                             | -        | Defines a string that labels the move to all left button for accessibility.                                                                                                                                                                                       |
| upButtonAriaLabel       | string                             | -        | Defines a string that labels the move to up button for accessibility.                                                                                                                                                                                             |
| downButtonAriaLabel     | string                             | -        | Defines a string that labels the move to down button for accessibility.                                                                                                                                                                                           |
| topButtonAriaLabel      | string                             | -        | Defines a string that labels the move to top button for accessibility.                                                                                                                                                                                            |
| bottomButtonAriaLabel   | string                             | -        | Defines a string that labels the move to bottom button for accessibility.                                                                                                                                                                                         |
| sourceAriaLabel         | string                             | -        | Defines a string that labels the source list.                                                                                                                                                                                                                     |
| targetAriaLabel         | string                             | -        | Defines a string that labels the target list.                                                                                                                                                                                                                     |
| targetHeader            | string                             | -        | Text for the target list caption                                                                                                                                                                                                                                  |
| responsive              | boolean                            | false    | When enabled orderlist adjusts its controls based on screen size.                                                                                                                                                                                                 |
| filterBy                | string                             | -        | When specified displays an input field to filter the items on keyup and decides which field to search (Accepts multiple fields with a comma).                                                                                                                     |
| filterLocale            | string                             | -        | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                                          |
| trackBy                 | Function                           | ...      | Function to optimize the dom operations by delegating to ngForTrackBy, default algorithm checks for object identity. Use sourceTrackBy or targetTrackBy in case different algorithms are needed per list.                                                         |
| sourceTrackBy           | Function                           | -        | Function to optimize the dom operations by delegating to ngForTrackBy in source list, default algorithm checks for object identity.                                                                                                                               |
| targetTrackBy           | Function                           | -        | Function to optimize the dom operations by delegating to ngForTrackBy in target list, default algorithm checks for object identity.                                                                                                                               |
| showSourceFilter        | boolean                            | true     | Whether to show filter input for source list when filterBy is enabled.                                                                                                                                                                                            |
| showTargetFilter        | boolean                            | true     | Whether to show filter input for target list when filterBy is enabled.                                                                                                                                                                                            |
| metaKeySelection        | boolean                            | false    | Defines how multiple items can be selected, when true metaKey needs to be pressed to select or unselect an item and when set to false selection of each item can be toggled individually. On touch enabled devices, metaKeySelection is turned off automatically. |
| dragdrop                | boolean                            | false    | Whether to enable dragdrop based reordering.                                                                                                                                                                                                                      |
| style                   | { [klass: string]: any }           | -        | Inline style of the component.                                                                                                                                                                                                                                    |
| styleClass              | string                             | -        | Style class of the component.                                                                                                                                                                                                                                     |
| sourceStyle             | any                                | -        | Inline style of the source list element.                                                                                                                                                                                                                          |
| targetStyle             | any                                | -        | Inline style of the target list element.                                                                                                                                                                                                                          |
| showSourceControls      | boolean                            | true     | Whether to show buttons of source list.                                                                                                                                                                                                                           |
| showTargetControls      | boolean                            | true     | Whether to show buttons of target list.                                                                                                                                                                                                                           |
| sourceFilterPlaceholder | string                             | -        | Placeholder text on source filter input.                                                                                                                                                                                                                          |
| targetFilterPlaceholder | string                             | -        | Placeholder text on target filter input.                                                                                                                                                                                                                          |
| disabled                | boolean                            | false    | When present, it specifies that the component should be disabled.                                                                                                                                                                                                 |
| sourceOptionDisabled    | string \| ((item: any) => boolean) | -        | Name of the disabled field of a target option or function to determine disabled state.                                                                                                                                                                            |
| targetOptionDisabled    | string \| ((item: any) => boolean) | -        | Name of the disabled field of a target option or function to determine disabled state.                                                                                                                                                                            |
| ariaSourceFilterLabel   | string                             | -        | Defines a string that labels the filter input of source list.                                                                                                                                                                                                     |
| ariaTargetFilterLabel   | string                             | -        | Defines a string that labels the filter input of target list.                                                                                                                                                                                                     |
| filterMatchMode         | string                             | contains | Defines how the items are filtered.                                                                                                                                                                                                                               |
| stripedRows             | boolean                            | false    | Whether to displays rows with alternating colors.                                                                                                                                                                                                                 |
| keepSelection           | boolean                            | false    | Keeps selection on the transfer list.                                                                                                                                                                                                                             |
| scrollHeight            | string                             | 14rem    | Height of the viewport, a scrollbar is defined if height of list exceeds this value.                                                                                                                                                                              |
| autoOptionFocus         | boolean                            | true     | Whether to focus on the first visible or selected element.                                                                                                                                                                                                        |
| buttonProps             | ButtonProps                        | ...      | Used to pass all properties of the ButtonProps to the Button component.                                                                                                                                                                                           |
| moveUpButtonProps       | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move up button inside the component.                                                                                                                                                                        |
| moveTopButtonProps      | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move top button inside the component.                                                                                                                                                                       |
| moveDownButtonProps     | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move down button inside the component.                                                                                                                                                                      |
| moveBottomButtonProps   | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move bottom button inside the component.                                                                                                                                                                    |
| moveToTargetProps       | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move to target button inside the component.                                                                                                                                                                 |
| moveAllToTargetProps    | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move all to target button inside the component.                                                                                                                                                             |
| moveToSourceProps       | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move to source button inside the component.                                                                                                                                                                 |
| moveAllToSourceProps    | ButtonProps                        | -        | Used to pass all properties of the ButtonProps to the move all to source button inside the component.                                                                                                                                                             |
| breakpoint              | string                             | -        | Indicates the width of the screen at which the component should change its behavior.                                                                                                                                                                              |

## Outputs

| Name              | Parameters                          | Description                                                        |
| ----------------- | ----------------------------------- | ------------------------------------------------------------------ |
| onMoveToSource    | event: PickListMoveToSourceEvent    | Callback to invoke when items are moved from target to source.     |
| onMoveAllToSource | event: PickListMoveAllToSourceEvent | Callback to invoke when all items are moved from target to source. |
| onMoveAllToTarget | event: PickListMoveAllToTargetEvent | Callback to invoke when all items are moved from source to target. |
| onMoveToTarget    | event: PickListMoveToTargetEvent    | Callback to invoke when items are moved from source to target.     |
| onSourceReorder   | event: PickListSourceReorderEvent   | Callback to invoke when items are reordered within source list.    |
| onTargetReorder   | event: PickListTargetReorderEvent   | Callback to invoke when items are reordered within target list.    |
| onSourceSelect    | event: PickListSourceSelectEvent    | Callback to invoke when items are selected within source list.     |
| onTargetSelect    | event: PickListTargetSelectEvent    | Callback to invoke when items are selected within target list.     |
| onSourceFilter    | event: PickListSourceFilterEvent    | Callback to invoke when the source list is filtered                |
| onTargetFilter    | event: PickListTargetFilterEvent    | Callback to invoke when the target list is filtered                |
| onFocus           | event: Event                        | Callback to invoke when the list is focused                        |
| onBlur            | event: Event                        | Callback to invoke when the list is blurred                        |

## Templates

| Name                     | Type                                             | Description                                                |
| ------------------------ | ------------------------------------------------ | ---------------------------------------------------------- |
| item                     | TemplateRef<PickListItemTemplateContext>         | Custom item template.                                      |
| sourceheader             | TemplateRef<void>                                | Custom source header template.                             |
| targetheader             | TemplateRef<void>                                | Custom target header template.                             |
| sourcefilter             | TemplateRef<PickListFilterTemplateContext>       | Custom source filter template.                             |
| targetfilter             | TemplateRef<PickListFilterTemplateContext>       | Custom target filter template.                             |
| emptymessagesource       | TemplateRef<void>                                | Custom empty message when source is empty template.        |
| emptyfiltermessagesource | TemplateRef<void>                                | Custom empty filter message when source is empty template. |
| emptymessagetarget       | TemplateRef<void>                                | Custom empty message when target is empty template.        |
| emptyfiltermessagetarget | TemplateRef<void>                                | Custom empty filter message when target is empty template. |
| moveupicon               | TemplateRef<void>                                | Custom move up icon template.                              |
| movetopicon              | TemplateRef<void>                                | Custom move top icon template.                             |
| movedownicon             | TemplateRef<void>                                | Custom move down icon template.                            |
| movebottomicon           | TemplateRef<void>                                | Custom move bottom icon template.                          |
| movetotargeticon         | TemplateRef<PickListTransferIconTemplateContext> | Custom move to target icon template.                       |
| movealltotargeticon      | TemplateRef<PickListTransferIconTemplateContext> | Custom move all to target icon template.                   |
| movetosourceicon         | TemplateRef<PickListTransferIconTemplateContext> | Custom move to source icon template.                       |
| movealltosourceicon      | TemplateRef<PickListTransferIconTemplateContext> | Custom move all to source icon template.                   |
| targetfiltericon         | TemplateRef<void>                                | Custom target filter icon template.                        |
| sourcefiltericon         | TemplateRef<void>                                | Custom source filter icon template.                        |

**Full API & more examples:** https://primeng.org/picklist
