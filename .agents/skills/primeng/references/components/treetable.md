# TreeTable (`p-treetable`)

TreeTable is used to display hierarchical data in tabular format.

**Import:**

```ts
import { TreeTableModule } from "primeng/treetable";
import { TreeNode } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit, inject } from "@angular/core";
import { TreeTableModule } from "primeng/treetable";
import { NodeService } from "@/service/nodeservice";
import { TreeNode } from "primeng/api";

@Component({
  template: `
    <p-treetable
      [value]="files"
      [scrollable]="true"
      [tableStyle]="{ 'min-width': '50rem' }"
    >
      <ng-template #header>
        <tr>
          <th>Name</th>
          <th>Size</th>
          <th>Type</th>
        </tr>
      </ng-template>
      <ng-template #body let-rowNode let-rowData="rowData">
        <tr [ttRow]="rowNode">
          <td>
            <div class="flex items-center gap-2">
              <p-treetable-toggler [rowNode]="rowNode" />
              <span>{{ rowData.name }}</span>
            </div>
          </td>
          <td>{{ rowData.size }}</td>
          <td>{{ rowData.type }}</td>
        </tr>
      </ng-template>
    </p-treetable>
  `,
  standalone: true,
  imports: [TreeTableModule],
  providers: [NodeService],
})
export class TreetableBasicDemo implements OnInit {
  private nodeService = inject(NodeService);
  files!: TreeNode[];

  ngOnInit() {
    this.nodeService.getFilesystem().then((files) => (this.files = files));
  }
}
```

## Inputs

| Name                      | Type                            | Default                       | Description                                                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| columns                   | any[]                           | -                             | An array of objects to represent dynamic columns.                                                                                                                                                                                                                       |
| tableStyle                | { [klass: string]: any }        | -                             | Inline style of the table.                                                                                                                                                                                                                                              |
| tableStyleClass           | string                          | -                             | Style class of the table.                                                                                                                                                                                                                                               |
| autoLayout                | boolean                         | false                         | Whether the cell widths scale according to their content or not.                                                                                                                                                                                                        |
| lazy                      | boolean                         | false                         | Defines if data is loaded and interacted with in lazy manner.                                                                                                                                                                                                           |
| lazyLoadOnInit            | boolean                         | true                          | Whether to call lazy loading on initialization.                                                                                                                                                                                                                         |
| paginator                 | boolean                         | false                         | When specified as true, enables the pagination.                                                                                                                                                                                                                         |
| rows                      | number                          | -                             | Number of rows to display per page.                                                                                                                                                                                                                                     |
| first                     | number                          | 0                             | Index of the first row to be displayed.                                                                                                                                                                                                                                 |
| pageLinks                 | number                          | 5                             | Number of page links to display in paginator.                                                                                                                                                                                                                           |
| rowsPerPageOptions        | any[]                           | -                             | Array of integer/object values to display inside rows per page dropdown of paginator                                                                                                                                                                                    |
| alwaysShowPaginator       | boolean                         | true                          | Whether to show it even there is only one page.                                                                                                                                                                                                                         |
| paginatorPosition         | "top" \| "bottom" \| "both"     | bottom                        | Position of the paginator.                                                                                                                                                                                                                                              |
| paginatorStyleClass       | string                          | -                             | Custom style class for paginator                                                                                                                                                                                                                                        |
| paginatorDropdownAppendTo | any                             | -                             | Target element to attach the paginator dropdown overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| currentPageReportTemplate | string                          | {currentPage} of {totalPages} | Template of the current page report element. Available placeholders are {currentPage},{totalPages},{rows},{first},{last} and {totalRecords}                                                                                                                             |
| showCurrentPageReport     | boolean                         | false                         | Whether to display current page report.                                                                                                                                                                                                                                 |
| showJumpToPageDropdown    | boolean                         | false                         | Whether to display a dropdown to navigate to any page.                                                                                                                                                                                                                  |
| showFirstLastIcon         | boolean                         | true                          | When enabled, icons are displayed on paginator to go first and last page.                                                                                                                                                                                               |
| showPageLinks             | boolean                         | true                          | Whether to show page links.                                                                                                                                                                                                                                             |
| defaultSortOrder          | number                          | 1                             | Sort order to use when an unsorted column gets sorted by user interaction.                                                                                                                                                                                              |
| sortMode                  | "multiple" \| "single"          | single                        | Defines whether sorting works on single column or on multiple columns.                                                                                                                                                                                                  |
| resetPageOnSort           | boolean                         | true                          | When true, resets paginator to first page after sorting.                                                                                                                                                                                                                |
| customSort                | boolean                         | false                         | Whether to use the default sorting or a custom one using sortFunction.                                                                                                                                                                                                  |
| selectionMode             | string                          | -                             | Specifies the selection mode, valid values are "single" and "multiple".                                                                                                                                                                                                 |
| contextMenuSelection      | any                             | -                             | Selected row with a context menu.                                                                                                                                                                                                                                       |
| contextMenuSelectionMode  | string                          | separate                      | Mode of the contet menu selection.                                                                                                                                                                                                                                      |
| dataKey                   | string                          | -                             | A property to uniquely identify a record in data.                                                                                                                                                                                                                       |
| metaKeySelection          | boolean                         | false                         | Defines whether metaKey is should be considered for the selection. On touch enabled devices, metaKeySelection is turned off automatically.                                                                                                                              |
| compareSelectionBy        | string                          | deepEquals                    | Algorithm to define if a row is selected, valid values are "equals" that compares by reference and "deepEquals" that compares all fields.                                                                                                                               |
| rowHover                  | boolean                         | false                         | Adds hover effect to rows without the need for selectionMode.                                                                                                                                                                                                           |
| loading                   | boolean                         | false                         | Displays a loader to indicate data load is in progress.                                                                                                                                                                                                                 |
| loadingIcon               | string                          | -                             | The icon to show while indicating data load is in progress.                                                                                                                                                                                                             |
| showLoader                | boolean                         | true                          | Whether to show the loading mask when loading property is true.                                                                                                                                                                                                         |
| scrollable                | boolean                         | false                         | When specified, enables horizontal and/or vertical scrolling.                                                                                                                                                                                                           |
| scrollHeight              | string                          | -                             | Height of the scroll viewport in fixed pixels or the "flex" keyword for a dynamic size.                                                                                                                                                                                 |
| virtualScroll             | boolean                         | false                         | Whether the data should be loaded on demand during scroll.                                                                                                                                                                                                              |
| virtualScrollItemSize     | number                          | -                             | Height of a row to use in calculations of virtual scrolling.                                                                                                                                                                                                            |
| virtualScrollOptions      | ScrollerOptions                 | -                             | Whether to use the scroller feature. The properties of scroller component can be used like an object in it.                                                                                                                                                             |
| virtualScrollDelay        | number                          | 150                           | The delay (in milliseconds) before triggering the virtual scroll. This determines the time gap between the user's scroll action and the actual rendering of the next set of items in the virtual scroll.                                                                |
| frozenWidth               | string                          | -                             | Width of the frozen columns container.                                                                                                                                                                                                                                  |
| frozenColumns             | { [klass: string]: any }        | -                             | An array of objects to represent dynamic columns that are frozen.                                                                                                                                                                                                       |
| resizableColumns          | boolean                         | false                         | When enabled, columns can be resized using drag and drop.                                                                                                                                                                                                               |
| columnResizeMode          | string                          | fit                           | Defines whether the overall table width should change on column resize, valid values are "fit" and "expand".                                                                                                                                                            |
| reorderableColumns        | boolean                         | false                         | When enabled, columns can be reordered using drag and drop.                                                                                                                                                                                                             |
| contextMenu               | any                             | -                             | Local ng-template varilable of a ContextMenu.                                                                                                                                                                                                                           |
| rowTrackBy                | Function                        | ...                           | Function to optimize the dom operations by delegating to ngForTrackBy, default algorithm checks for object identity.                                                                                                                                                    |
| filters                   | { [s: string]: FilterMetadata } | {}                            | An array of FilterMetadata objects to provide external filters.                                                                                                                                                                                                         |
| globalFilterFields        | string[]                        | -                             | An array of fields as string to use in global filtering.                                                                                                                                                                                                                |
| filterDelay               | number                          | 300                           | Delay in milliseconds before filtering the data.                                                                                                                                                                                                                        |
| filterMode                | string                          | lenient                       | Mode for filtering valid values are "lenient" and "strict". Default is lenient.                                                                                                                                                                                         |
| filterLocale              | string                          | -                             | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                                                |
| paginatorLocale           | string                          | -                             | Locale to be used in paginator formatting.                                                                                                                                                                                                                              |
| totalRecords              | number                          | -                             | Number of total records, defaults to length of value when not defined.                                                                                                                                                                                                  |
| sortField                 | string                          | -                             | Name of the field to sort data by default.                                                                                                                                                                                                                              |
| sortOrder                 | number                          | -                             | Order to sort when default sorting is enabled.                                                                                                                                                                                                                          |
| multiSortMeta             | SortMeta[]                      | -                             | An array of SortMeta objects to sort the data by default in multiple sort mode.                                                                                                                                                                                         |
| selection                 | any                             | -                             | Selected row in single mode or an array of values in multiple mode.                                                                                                                                                                                                     |
| value                     | TreeNode<any>[]                 | -                             | An array of objects to display.                                                                                                                                                                                                                                         |
| selectionKeys             | any                             | -                             | A map of keys to control the selection state.                                                                                                                                                                                                                           |
| showGridlines             | boolean                         | false                         | Whether to show grid lines between cells.                                                                                                                                                                                                                               |

## Outputs

| Name                       | Parameters                                | Description                                                                         |
| -------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------- |
| selectionChange            | value: TreeTableNode<any                  | Callback to invoke on selected node change.                                         |
| contextMenuSelectionChange | value: TreeTableNode<any                  | Callback to invoke on context menu selection change.                                |
| onFilter                   | event: TreeTableFilterEvent               | Callback to invoke when data is filtered.                                           |
| onNodeExpand               | event: TreeTableNodeExpandEvent<any       | Callback to invoke when a node is expanded.                                         |
| onNodeCollapse             | event: TreeTableNodeCollapseEvent<any     | Callback to invoke when a node is collapsed.                                        |
| onPage                     | value: TreeTablePaginatorState            | Callback to invoke when pagination occurs.                                          |
| onSort                     | value: any                                | Callback to invoke when a column gets sorted.                                       |
| onLazyLoad                 | event: TreeTableLazyLoadEvent             | Callback to invoke when paging, sorting or filtering happens in lazy mode.          |
| sortFunction               | event: TreeTableSortEvent                 | An event emitter to invoke on custom sorting, refer to sorting section for details. |
| onColResize                | event: TreeTableColResizeEvent            | Callback to invoke when a column is resized.                                        |
| onColReorder               | event: TreeTableColumnReorderEvent        | Callback to invoke when a column is reordered.                                      |
| onNodeSelect               | value: TreeTableNode<any                  | Callback to invoke when a node is selected.                                         |
| onNodeUnselect             | event: TreeTableNodeUnSelectEvent         | Callback to invoke when a node is unselected.                                       |
| onContextMenuSelect        | event: TreeTableContextMenuSelectEvent    | Callback to invoke when a node is selected with right click.                        |
| onHeaderCheckboxToggle     | event: TreeTableHeaderCheckboxToggleEvent | Callback to invoke when state of header checkbox changes.                           |
| onEditInit                 | event: TreeTableEditEvent                 | Callback to invoke when a cell switches to edit mode.                               |
| onEditComplete             | event: TreeTableEditEvent                 | Callback to invoke when cell edit is completed.                                     |
| onEditCancel               | event: TreeTableEditEvent                 | Callback to invoke when cell edit is cancelled with escape key.                     |
| selectionKeysChange        | value: any                                | Callback to invoke when selectionKeys are changed.                                  |

## Methods

| Name                 | Parameters               | Return Type | Description                                       |
| -------------------- | ------------------------ | ----------- | ------------------------------------------------- |
| resetScrollTop       |                          | void        | Resets scroll to top.                             |
| scrollToVirtualIndex | index: number            | void        | Scrolls to given index when using virtual scroll. |
| scrollTo             | options: ScrollToOptions | void        | Scrolls to given index.                           |
| reset                |                          | void        | Clears the sort and paginator state.              |

**Full API & more examples:** https://primeng.org/treetable
