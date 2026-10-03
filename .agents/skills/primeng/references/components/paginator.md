# Paginator (`p-paginator`)

Paginator displays data in paged format and provides navigation between pages.

**Import:**

```ts
import { Paginator, PaginatorModule } from "primeng/paginator";
```

## Example

```typescript
import { Component } from "@angular/core";
import { Paginator, PaginatorModule } from "primeng/paginator";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-paginator
        (onPageChange)="onPageChange($event)"
        [first]="first"
        [rows]="rows"
        [totalRecords]="120"
        [rowsPerPageOptions]="[10, 20, 30]"
      />
    </div>
  `,
  standalone: true,
  imports: [PaginatorModule],
})
export class PaginatorBasicDemo {
  first: number = 0;
  rows: number = 10;

  onPageChange(event: PaginatorState) {
    this.first = event.first ?? 0;
    this.rows = event.rows ?? 10;
  }
}
```

## Inputs

| Name                      | Type                                              | Default                       | Description                                                                                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pageLinkSize              | number                                            | 5                             | Number of page links to display.                                                                                                                                                                                                                     |
| alwaysShow                | boolean                                           | true                          | Whether to show it even there is only one page.                                                                                                                                                                                                      |
| templateLeft              | TemplateRef<PaginatorTemplateContext>             | -                             | Template instance to inject into the left side of the paginator.                                                                                                                                                                                     |
| templateRight             | TemplateRef<PaginatorTemplateContext>             | -                             | Template instance to inject into the right side of the paginator.                                                                                                                                                                                    |
| dropdownScrollHeight      | string                                            | 200px                         | Dropdown height of the viewport in pixels, a scrollbar is defined if height of list exceeds this value.                                                                                                                                              |
| currentPageReportTemplate | string                                            | {currentPage} of {totalPages} | Template of the current page report element. Available placeholders are {currentPage},{totalPages},{rows},{first},{last} and {totalRecords}                                                                                                          |
| showCurrentPageReport     | boolean                                           | false                         | Whether to display current page report.                                                                                                                                                                                                              |
| showFirstLastIcon         | boolean                                           | true                          | When enabled, icons are displayed on paginator to go first and last page.                                                                                                                                                                            |
| totalRecords              | number                                            | 0                             | Number of total records.                                                                                                                                                                                                                             |
| rows                      | number                                            | 0                             | Data count to display per page.                                                                                                                                                                                                                      |
| rowsPerPageOptions        | any[]                                             | -                             | Array of integer/object values to display inside rows per page dropdown. A object that have 'showAll' key can be added to it to show all data. Exp; [10,20,30,{showAll:'All'}]                                                                       |
| showJumpToPageDropdown    | boolean                                           | false                         | Whether to display a dropdown to navigate to any page.                                                                                                                                                                                               |
| showJumpToPageInput       | boolean                                           | false                         | Whether to display a input to navigate to any page.                                                                                                                                                                                                  |
| jumpToPageItemTemplate    | TemplateRef<PaginatorDropdownItemTemplateContext> | -                             | Template instance to inject into the jump to page dropdown item inside in the paginator.                                                                                                                                                             |
| showPageLinks             | boolean                                           | true                          | Whether to show page links.                                                                                                                                                                                                                          |
| locale                    | string                                            | -                             | Locale to be used in formatting.                                                                                                                                                                                                                     |
| dropdownItemTemplate      | TemplateRef<PaginatorDropdownItemTemplateContext> | -                             | Template instance to inject into the rows per page dropdown item inside in the paginator.                                                                                                                                                            |
| first                     | number                                            | -                             | Zero-relative number of the first row to be displayed.                                                                                                                                                                                               |
| appendTo                  | InputSignal<any>                                  | 'self'                        | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |

## Outputs

| Name         | Parameters            | Description                                                                                      |
| ------------ | --------------------- | ------------------------------------------------------------------------------------------------ |
| onPageChange | value: PaginatorState | Callback to invoke when page changes, the event object contains information about the new state. |

## Templates

| Name                 | Type              | Description                               |
| -------------------- | ----------------- | ----------------------------------------- |
| dropdownicon         | TemplateRef<void> | Template for the dropdown icon.           |
| firstpagelinkicon    | TemplateRef<void> | Template for the first page link icon.    |
| previouspagelinkicon | TemplateRef<void> | Template for the previous page link icon. |
| lastpagelinkicon     | TemplateRef<void> | Template for the last page link icon.     |
| nextpagelinkicon     | TemplateRef<void> | Template for the next page link icon.     |

**Full API & more examples:** https://primeng.org/paginator
