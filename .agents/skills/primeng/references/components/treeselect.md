# TreeSelect (`p-treeselect`)

TreeSelect is a form component to choose from hierarchical data.

**Import:**

```ts
import { TreeSelectModule } from "primeng/treeselect";
import { TreeNode } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit, inject } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { TreeSelectModule } from "primeng/treeselect";
import { NodeService } from "@/service/nodeservice";
import { TreeNode } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-treeselect
        class="md:w-80 w-full"
        [(ngModel)]="selectedNodes"
        [options]="nodes"
        placeholder="Select Item"
      />
    </div>
  `,
  standalone: true,
  imports: [TreeSelectModule, FormsModule],
  providers: [NodeService],
})
export class TreeselectBasicDemo implements OnInit {
  private nodeService = inject(NodeService);
  nodes!: any[];
  selectedNodes: any;

  constructor() {
    this.nodeService.getFiles().then((files) => (this.nodes = files));
  }

  ngOnInit() {}
}
```

## Inputs

| Name                   | Type                                                          | Default   | Description                                                                                                                                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required               | InputSignalWithTransform<boolean, unknown>                    | false     | There must be a value (if set).                                                                                                                                                                                                                                   |
| invalid                | InputSignalWithTransform<boolean, unknown>                    | false     | When present, it specifies that the component should have invalid state style.                                                                                                                                                                                    |
| disabled               | InputSignalWithTransform<boolean, unknown>                    | false     | When present, it specifies that the component should have disabled state style.                                                                                                                                                                                   |
| name                   | InputSignal<string>                                           | undefined | When present, it specifies that the name of the input.                                                                                                                                                                                                            |
| inputId                | string                                                        | -         | Identifier of the underlying input element.                                                                                                                                                                                                                       |
| scrollHeight           | string                                                        | 400px     | Height of the viewport, a scrollbar is defined if height of list exceeds this value.                                                                                                                                                                              |
| metaKeySelection       | boolean                                                       | false     | Defines how multiple items can be selected, when true metaKey needs to be pressed to select or unselect an item and when set to false selection of each item can be toggled individually. On touch enabled devices, metaKeySelection is turned off automatically. |
| display                | "chip" \| "comma"                                             | comma     | Defines how the selected items are displayed.                                                                                                                                                                                                                     |
| selectionMode          | "multiple" \| "single" \| "checkbox"                          | single    | Defines the selection mode.                                                                                                                                                                                                                                       |
| tabindex               | string                                                        | 0         | Index of the element in tabbing order.                                                                                                                                                                                                                            |
| ariaLabel              | string                                                        | -         | Defines a string that labels the input for accessibility.                                                                                                                                                                                                         |
| ariaLabelledBy         | string                                                        | -         | Establishes relationships between the component and label(s) where its value should be one or more element IDs.                                                                                                                                                   |
| placeholder            | string                                                        | -         | Label to display when there are no selections.                                                                                                                                                                                                                    |
| panelClass             | string \| string[] \| Set<string> \| { [klass: string]: any } | -         | Style class of the overlay panel.                                                                                                                                                                                                                                 |
| panelStyle             | { [klass: string]: any }                                      | -         | Inline style of the panel element.                                                                                                                                                                                                                                |
| panelStyleClass        | string                                                        | -         | Style class of the panel element.                                                                                                                                                                                                                                 |
| labelStyle             | { [klass: string]: any }                                      | -         | Inline style of the label element.                                                                                                                                                                                                                                |
| labelStyleClass        | string                                                        | -         | Style class of the label element.                                                                                                                                                                                                                                 |
| overlayOptions         | OverlayOptions                                                | -         | Specifies the options for the overlay.                                                                                                                                                                                                                            |
| emptyMessage           | string                                                        | -         | Text to display when there are no options available. Defaults to value from PrimeNG locale configuration.                                                                                                                                                         |
| filter                 | boolean                                                       | false     | When specified, displays an input field to filter the items.                                                                                                                                                                                                      |
| filterBy               | string                                                        | label     | When filtering is enabled, filterBy decides which field or fields (comma separated) to search against.                                                                                                                                                            |
| filterMode             | string                                                        | lenient   | Mode for filtering valid values are "lenient" and "strict". Default is lenient.                                                                                                                                                                                   |
| filterPlaceholder      | string                                                        | -         | Placeholder text to show when filter input is empty.                                                                                                                                                                                                              |
| filterLocale           | string                                                        | -         | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                                          |
| filterInputAutoFocus   | boolean                                                       | true      | Determines whether the filter input should be automatically focused when the component is rendered.                                                                                                                                                               |
| propagateSelectionDown | boolean                                                       | true      | Whether checkbox selections propagate to descendant nodes.                                                                                                                                                                                                        |
| propagateSelectionUp   | boolean                                                       | true      | Whether checkbox selections propagate to ancestor nodes.                                                                                                                                                                                                          |
| showClear              | boolean                                                       | false     | When enabled, a clear icon is displayed to clear the value.                                                                                                                                                                                                       |
| resetFilterOnHide      | boolean                                                       | true      | Clears the filter value when hiding the dropdown.                                                                                                                                                                                                                 |
| virtualScroll          | boolean                                                       | false     | Whether the data should be loaded on demand during scroll.                                                                                                                                                                                                        |
| virtualScrollItemSize  | number                                                        | -         | Height of an item in the list for VirtualScrolling.                                                                                                                                                                                                               |
| virtualScrollOptions   | ScrollerOptions                                               | -         | Whether to use the scroller feature. The properties of scroller component can be used like an object in it.                                                                                                                                                       |
| autofocus              | boolean                                                       | false     | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                             |
| options                | TreeNode<any>[]                                               | -         | An array of treenodes.                                                                                                                                                                                                                                            |
| loading                | boolean                                                       | false     | Displays a loader to indicate data load is in progress.                                                                                                                                                                                                           |
| loadingMode            | "icon" \| "mask"                                              | mask      | Loading mode display.                                                                                                                                                                                                                                             |
| size                   | InputSignal<"small" \| "large">                               | undefined | Specifies the size of the component.                                                                                                                                                                                                                              |
| variant                | InputSignal<"outlined" \| "filled">                           | undefined | Specifies the input variant of the component.                                                                                                                                                                                                                     |
| fluid                  | InputSignalWithTransform<boolean, unknown>                    | undefined | Spans 100% width of the container when enabled.                                                                                                                                                                                                                   |
| appendTo               | InputSignal<any>                                              | 'self'    | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name).              |
| motionOptions          | InputSignal<MotionOptions>                                    | ...       | The motion options.                                                                                                                                                                                                                                               |

## Outputs

| Name           | Parameters                         | Description                                     |
| -------------- | ---------------------------------- | ----------------------------------------------- |
| onNodeExpand   | event: TreeSelectNodeExpandEvent   | Callback to invoke when a node is expanded.     |
| onNodeCollapse | event: TreeSelectNodeCollapseEvent | Callback to invoke when a node is collapsed.    |
| onShow         | value: any                         | Callback to invoke when the overlay is shown.   |
| onHide         | event: Event                       | Callback to invoke when the overlay is hidden.  |
| onClear        | value: any                         | Callback to invoke when input field is cleared. |
| onFilter       | event: TreeFilterEvent             | Callback to invoke when data is filtered.       |
| onFocus        | event: Event                       | Callback to invoke when treeselect gets focus.  |
| onBlur         | event: Event                       | Callback to invoke when treeselect loses focus. |
| onNodeUnselect | event: TreeNodeUnSelectEvent       | Callback to invoke when a node is unselected.   |
| onNodeSelect   | event: TreeNodeSelectEvent         | Callback to invoke when a node is selected.     |

## Templates

| Name             | Type                                                   | Description                         |
| ---------------- | ------------------------------------------------------ | ----------------------------------- |
| value            | TemplateRef<TreeSelectValueTemplateContext>            | Custom value template.              |
| header           | TemplateRef<TreeSelectHeaderTemplateContext>           | Custom header template.             |
| empty            | TemplateRef<void>                                      | Custom empty message template.      |
| footer           | TemplateRef<TreeSelectHeaderTemplateContext>           | Custom footer template.             |
| clearicon        | TemplateRef<void>                                      | Custom clear icon template.         |
| triggericon      | TemplateRef<void>                                      | Custom trigger icon template.       |
| dropdownicon     | TemplateRef<void>                                      | Custom dropdown icon template.      |
| filtericon       | TemplateRef<void>                                      | Custom filter icon template.        |
| closeicon        | TemplateRef<void>                                      | Custom close icon template.         |
| itemtogglericon  | TemplateRef<TreeSelectItemTogglerIconTemplateContext>  | Custom item toggler icon template.  |
| itemcheckboxicon | TemplateRef<TreeSelectItemCheckboxIconTemplateContext> | Custom item checkbox icon template. |
| itemloadingicon  | TemplateRef<void>                                      | Custom item loading icon template.  |

**Full API & more examples:** https://primeng.org/treeselect
