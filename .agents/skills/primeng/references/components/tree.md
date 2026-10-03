# Tree (`p-tree`)

Tree is used to display hierarchical data.

**Import:**

```ts
import { TreeModule } from "primeng/tree";
import { TreeNode } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit, inject, signal } from "@angular/core";
import { TreeModule } from "primeng/tree";
import { NodeService } from "@/service/nodeservice";
import { TreeNode } from "primeng/api";

@Component({
  template: `
    <div class="card">
      <p-tree [value]="files()" class="w-full md:w-[30rem]" />
    </div>
  `,
  standalone: true,
  imports: [TreeModule],
  providers: [NodeService],
})
export class TreeBasicDemo implements OnInit {
  private nodeService = inject(NodeService);
  files = signal<TreeNode[]>(undefined);

  ngOnInit() {
    this.nodeService.getFiles().then((data) => {
      this.files.set(data);
    });
  }
}
```

## Inputs

| Name                     | Type                                          | Default | Description                                                                                                                                                                                                                                                                                |
| ------------------------ | --------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| value                    | any                                           | -       | An array of treenodes.                                                                                                                                                                                                                                                                     |
| selectionMode            | "multiple" \| "single" \| "checkbox"          | -       | Defines the selection mode.                                                                                                                                                                                                                                                                |
| loadingMode              | "icon" \| "mask"                              | mask    | Loading mode display.                                                                                                                                                                                                                                                                      |
| selection                | ModelSignal<TreeNode<any> \| TreeNode<any>[]> | ...     | A single treenode instance or an array to refer to the selections.                                                                                                                                                                                                                         |
| contextMenu              | any                                           | -       | Context menu instance.                                                                                                                                                                                                                                                                     |
| contextMenuSelectionMode | "separate" \| "joint"                         | joint   | Defines the behavior of context menu selection, in "separate" mode context menu updates contextMenuSelection property whereas in joint mode selection property is used instead so that when row selection is enabled, both row selection and context menu selection use the same property. |
| contextMenuSelection     | ModelSignal<TreeNode<any>>                    | ...     | Selected node with a context menu.                                                                                                                                                                                                                                                         |
| draggableScope           | any                                           | -       | Scope of the draggable nodes to match a droppableScope.                                                                                                                                                                                                                                    |
| droppableScope           | any                                           | -       | Scope of the droppable nodes to match a draggableScope.                                                                                                                                                                                                                                    |
| draggableNodes           | boolean                                       | false   | Whether the nodes are draggable.                                                                                                                                                                                                                                                           |
| droppableNodes           | boolean                                       | false   | Whether the nodes are droppable.                                                                                                                                                                                                                                                           |
| metaKeySelection         | boolean                                       | false   | Defines how multiple items can be selected, when true metaKey needs to be pressed to select or unselect an item and when set to false selection of each item can be toggled individually. On touch enabled devices, metaKeySelection is turned off automatically.                          |
| propagateSelectionUp     | boolean                                       | true    | Whether checkbox selections propagate to ancestor nodes.                                                                                                                                                                                                                                   |
| propagateSelectionDown   | boolean                                       | true    | Whether checkbox selections propagate to descendant nodes.                                                                                                                                                                                                                                 |
| loading                  | boolean                                       | false   | Displays a loader to indicate data load is in progress.                                                                                                                                                                                                                                    |
| loadingIcon              | string                                        | -       | The icon to show while indicating data load is in progress.                                                                                                                                                                                                                                |
| emptyMessage             | string                                        | -       | Text to display when there is no data.                                                                                                                                                                                                                                                     |
| ariaLabel                | string                                        | -       | Used to define a string that labels the tree.                                                                                                                                                                                                                                              |
| togglerAriaLabel         | string                                        | -       | Defines a string that labels the toggler icon for accessibility.                                                                                                                                                                                                                           |
| ariaLabelledBy           | string                                        | -       | Establishes relationships between the component and label(s) where its value should be one or more element IDs.                                                                                                                                                                            |
| validateDrop             | boolean                                       | false   | When enabled, drop can be accepted or rejected based on condition defined at onNodeDrop.                                                                                                                                                                                                   |
| filter                   | boolean                                       | false   | When specified, displays an input field to filter the items.                                                                                                                                                                                                                               |
| filterInputAutoFocus     | boolean                                       | false   | Determines whether the filter input should be automatically focused when the component is rendered.                                                                                                                                                                                        |
| filterBy                 | string                                        | label   | When filtering is enabled, filterBy decides which field or fields (comma separated) to search against.                                                                                                                                                                                     |
| filterMode               | string                                        | lenient | Mode for filtering valid values are "lenient" and "strict". Default is lenient.                                                                                                                                                                                                            |
| filterOptions            | any                                           | -       | Mode for filtering valid values are "lenient" and "strict". Default is lenient.                                                                                                                                                                                                            |
| filterPlaceholder        | string                                        | -       | Placeholder text to show when filter input is empty.                                                                                                                                                                                                                                       |
| filteredNodes            | TreeNode<any>[]                               | -       | Values after the tree nodes are filtered.                                                                                                                                                                                                                                                  |
| filterLocale             | string                                        | -       | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                                                                   |
| scrollHeight             | string                                        | -       | Height of the scrollable viewport.                                                                                                                                                                                                                                                         |
| lazy                     | boolean                                       | false   | Defines if data is loaded and interacted with in lazy manner.                                                                                                                                                                                                                              |
| virtualScroll            | boolean                                       | false   | Whether the data should be loaded on demand during scroll.                                                                                                                                                                                                                                 |
| virtualScrollItemSize    | number                                        | -       | Height of an item in the list for VirtualScrolling.                                                                                                                                                                                                                                        |
| virtualScrollOptions     | ScrollerOptions                               | -       | Whether to use the scroller feature. The properties of scroller component can be used like an object in it.                                                                                                                                                                                |
| indentation              | number                                        | 1.5     | Indentation factor for spacing of the nested node when virtual scrolling is enabled.                                                                                                                                                                                                       |
| \_templateMap            | any                                           | -       | Custom templates of the component.                                                                                                                                                                                                                                                         |
| trackBy                  | Function                                      | ...     | Function to optimize the node list rendering, default algorithm checks for object identity.                                                                                                                                                                                                |
| highlightOnSelect        | boolean                                       | false   | Highlights the node on select.                                                                                                                                                                                                                                                             |

## Outputs

| Name                    | Parameters                            | Description                                                                                      |
| ----------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| onNodeSelect            | event: TreeNodeSelectEvent            | Callback to invoke when a node is selected.                                                      |
| onNodeUnselect          | event: TreeNodeUnSelectEvent          | Callback to invoke when a node is unselected.                                                    |
| onNodeExpand            | event: TreeNodeExpandEvent            | Callback to invoke when a node is expanded.                                                      |
| onNodeCollapse          | event: TreeNodeCollapseEvent          | Callback to invoke when a node is collapsed.                                                     |
| onNodeContextMenuSelect | event: TreeNodeContextMenuSelectEvent | Callback to invoke when a node is selected with right click.                                     |
| onNodeDoubleClick       | event: TreeNodeDoubleClickEvent       | Callback to invoke when a node is double clicked.                                                |
| onNodeDrop              | event: TreeNodeDropEvent              | Callback to invoke when a node is dropped.                                                       |
| onLazyLoad              | event: TreeLazyLoadEvent              | Callback to invoke in lazy mode to load new data.                                                |
| onScroll                | event: TreeScrollEvent                | Callback to invoke in virtual scroll mode when scroll position changes.                          |
| onScrollIndexChange     | event: TreeScrollIndexChangeEvent     | Callback to invoke in virtual scroll mode when scroll position and item's range in view changes. |
| onFilter                | event: TreeFilterEvent                | Callback to invoke when data is filtered.                                                        |

## Templates

| Name         | Type                                         | Description                    |
| ------------ | -------------------------------------------- | ------------------------------ |
| filter       | TemplateRef<TreeFilterTemplateContext>       | Custom filter template.        |
| node         | TemplateRef<any>                             | Custom node template.          |
| header       | TemplateRef<void>                            | Custom header template.        |
| footer       | TemplateRef<void>                            | Custom footer template.        |
| loader       | TemplateRef<TreeLoaderTemplateContext>       | Custom loader template.        |
| empty        | TemplateRef<void>                            | Custom empty message template. |
| togglericon  | TemplateRef<TreeTogglerIconTemplateContext>  | Custom toggler icon template.  |
| checkboxicon | TemplateRef<TreeCheckboxIconTemplateContext> | Custom checkbox icon template. |
| loadingicon  | TemplateRef<void>                            | Custom loading icon template.  |
| filtericon   | TemplateRef<void>                            | Custom filter icon template.   |

## Methods

| Name                 | Parameters    | Return Type | Description               |
| -------------------- | ------------- | ----------- | ------------------------- |
| resetFilter          |               | void        | Resets filter.            |
| scrollToVirtualIndex | index: number | void        | Scrolls to virtual index. |
| scrollTo             | options: any  | void        | Scrolls to virtual index. |

**Full API & more examples:** https://primeng.org/tree
