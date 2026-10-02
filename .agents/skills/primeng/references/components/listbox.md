# Listbox (`p-listbox`)

Listbox is used to select one or more values from a list of items.

**Import:**

```ts
import { ListboxModule } from "primeng/listbox";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { ListboxModule } from "primeng/listbox";

interface City {
  name: string;
  code: string;
}

@Component({
  template: `
    <div class="card flex justify-center">
      <p-listbox
        [options]="cities"
        [(ngModel)]="selectedCity"
        optionLabel="name"
        class="w-full md:w-56"
      />
    </div>
  `,
  standalone: true,
  imports: [ListboxModule, FormsModule],
})
export class ListboxBasicDemo implements OnInit {
  cities!: City[];
  selectedCity!: City;

  ngOnInit() {
    this.cities = [
      { name: "New York", code: "NY" },
      { name: "Rome", code: "RM" },
      { name: "London", code: "LDN" },
      { name: "Istanbul", code: "IST" },
      { name: "Paris", code: "PRS" },
    ];
  }
}
```

## Inputs

| Name                  | Type                                       | Default                     | Description                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------ | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required              | InputSignalWithTransform<boolean, unknown> | false                       | There must be a value (if set).                                                                                                                                                                                                                                   |
| invalid               | InputSignalWithTransform<boolean, unknown> | false                       | When present, it specifies that the component should have invalid state style.                                                                                                                                                                                    |
| disabled              | InputSignalWithTransform<boolean, unknown> | false                       | When present, it specifies that the component should have disabled state style.                                                                                                                                                                                   |
| name                  | InputSignal<string>                        | undefined                   | When present, it specifies that the name of the input.                                                                                                                                                                                                            |
| id                    | string                                     | -                           | Unique identifier of the component.                                                                                                                                                                                                                               |
| searchMessage         | string                                     | '{0} results are available' | Text to display when the search is active. Defaults to global value in i18n translation configuration.                                                                                                                                                            |
| emptySelectionMessage | string                                     | 'No selected item'          | Text to display when filtering does not return any results. Defaults to global value in i18n translation configuration.                                                                                                                                           |
| selectionMessage      | string                                     | '{0} items selected'        | Text to be displayed in hidden accessible field when options are selected. Defaults to global value in i18n translation configuration.                                                                                                                            |
| autoOptionFocus       | boolean                                    | true                        | Whether to focus on the first visible or selected element when the overlay panel is shown.                                                                                                                                                                        |
| ariaLabel             | string                                     | -                           | Defines a string that labels the input for accessibility.                                                                                                                                                                                                         |
| selectOnFocus         | boolean                                    | false                       | When enabled, the focused option is selected.                                                                                                                                                                                                                     |
| searchLocale          | boolean                                    | false                       | Locale to use in searching. The default locale is the host environment's current locale.                                                                                                                                                                          |
| focusOnHover          | boolean                                    | true                        | When enabled, the hovered option will be focused.                                                                                                                                                                                                                 |
| filterMessage         | string                                     | -                           | Text to display when filtering.                                                                                                                                                                                                                                   |
| filterFields          | any[]                                      | -                           | Fields used when filtering the options, defaults to optionLabel.                                                                                                                                                                                                  |
| lazy                  | boolean                                    | false                       | Defines if data is loaded and interacted with in lazy manner.                                                                                                                                                                                                     |
| virtualScroll         | boolean                                    | false                       | Whether the data should be loaded on demand during scroll.                                                                                                                                                                                                        |
| virtualScrollItemSize | number                                     | -                           | Height of an item in the list for VirtualScrolling.                                                                                                                                                                                                               |
| virtualScrollOptions  | ScrollerOptions                            | -                           | Whether to use the scroller feature. The properties of scroller component can be used like an object in it.                                                                                                                                                       |
| scrollHeight          | string                                     | 14rem                       | Height of the viewport in pixels, a scrollbar is defined if height of list exceeds this value.                                                                                                                                                                    |
| tabindex              | number                                     | 0                           | Index of the element in tabbing order.                                                                                                                                                                                                                            |
| multiple              | boolean                                    | false                       | When specified, allows selecting multiple values.                                                                                                                                                                                                                 |
| listStyle             | { [klass: string]: any }                   | -                           | Inline style of the list element.                                                                                                                                                                                                                                 |
| listStyleClass        | string                                     | -                           | Style class of the list element.                                                                                                                                                                                                                                  |
| readonly              | boolean                                    | false                       | When present, it specifies that the element value cannot be changed.                                                                                                                                                                                              |
| checkbox              | boolean                                    | false                       | When specified, allows selecting items with checkboxes.                                                                                                                                                                                                           |
| filter                | boolean                                    | false                       | When specified, displays a filter input at header.                                                                                                                                                                                                                |
| filterBy              | string                                     | -                           | When filtering is enabled, filterBy decides which field or fields (comma separated) to search against.                                                                                                                                                            |
| filterMatchMode       | string                                     | contains                    | Defines how the items are filtered.                                                                                                                                                                                                                               |
| filterLocale          | string                                     | -                           | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                                          |
| metaKeySelection      | boolean                                    | false                       | Defines how multiple items can be selected, when true metaKey needs to be pressed to select or unselect an item and when set to false selection of each item can be toggled individually. On touch enabled devices, metaKeySelection is turned off automatically. |
| dataKey               | string                                     | -                           | A property to uniquely identify a value in options.                                                                                                                                                                                                               |
| showToggleAll         | boolean                                    | true                        | Whether header checkbox is shown in multiple mode.                                                                                                                                                                                                                |
| optionLabel           | string                                     | -                           | Name of the label field of an option.                                                                                                                                                                                                                             |
| optionValue           | string                                     | -                           | Name of the value field of an option.                                                                                                                                                                                                                             |
| optionGroupChildren   | string                                     | items                       | Name of the options field of an option group.                                                                                                                                                                                                                     |
| optionGroupLabel      | string                                     | label                       | Name of the label field of an option group.                                                                                                                                                                                                                       |
| optionDisabled        | string \| ((item: any) => boolean)         | -                           | Name of the disabled field of an option or function to determine disabled state.                                                                                                                                                                                  |
| ariaFilterLabel       | string                                     | -                           | Defines a string that labels the filter input.                                                                                                                                                                                                                    |
| filterPlaceHolder     | string                                     | -                           | Defines placeholder of the filter input.                                                                                                                                                                                                                          |
| emptyFilterMessage    | string                                     | -                           | Text to display when filtering does not return any results.                                                                                                                                                                                                       |
| emptyMessage          | string                                     | -                           | Text to display when there is no data. Defaults to global value in i18n translation configuration.                                                                                                                                                                |
| group                 | boolean                                    | false                       | Whether to display options as grouped when nested options are provided.                                                                                                                                                                                           |
| options               | any[]                                      | -                           | An array of selectitems to display as the available options.                                                                                                                                                                                                      |
| filterValue           | string                                     | -                           | When specified, filter displays with this value.                                                                                                                                                                                                                  |
| selectAll             | boolean                                    | -                           | Whether all data is selected.                                                                                                                                                                                                                                     |
| striped               | boolean                                    | false                       | Whether to displays rows with alternating colors.                                                                                                                                                                                                                 |
| highlightOnSelect     | boolean                                    | true                        | Whether the selected option will be add highlight class.                                                                                                                                                                                                          |
| checkmark             | boolean                                    | false                       | Whether the selected option will be shown with a check mark.                                                                                                                                                                                                      |
| dragdrop              | boolean                                    | false                       | Whether to enable dragdrop based reordering.                                                                                                                                                                                                                      |
| dropListData          | any[]                                      | -                           | Array to use for CDK drop list data binding. When not provided, uses options array.                                                                                                                                                                               |
| fluid                 | InputSignalWithTransform<boolean, unknown> | undefined                   | Spans 100% width of the container when enabled.                                                                                                                                                                                                                   |

## Outputs

| Name              | Parameters                                 | Description                                       |
| ----------------- | ------------------------------------------ | ------------------------------------------------- |
| onChange          | event: ListboxChangeEvent                  | Callback to invoke on value change.               |
| onClick           | event: ListboxClickEvent                   | Callback to invoke when option is clicked.        |
| onDblClick        | event: ListboxDoubleClickEvent             | Callback to invoke when option is double clicked. |
| onFilter          | event: ListboxFilterEvent                  | Callback to invoke when data is filtered.         |
| onFocus           | event: FocusEvent                          | Callback to invoke when component receives focus. |
| onBlur            | event: FocusEvent                          | Callback to invoke when component loses focus.    |
| onSelectAllChange | event: ListboxSelectAllChangeEvent         | Callback to invoke when all data is selected.     |
| onLazyLoad        | event: ScrollerLazyLoadEvent               | Emits on lazy load.                               |
| onDrop            | value: CdkDragDrop<string[], string[], any | Emits on item is dropped.                         |

## Templates

| Name        | Type                                           | Description                           |
| ----------- | ---------------------------------------------- | ------------------------------------- |
| item        | TemplateRef<ListboxItemTemplateContext<any>>   | Custom item template.                 |
| group       | TemplateRef<ListboxGroupTemplateContext<any>>  | Custom group template.                |
| header      | TemplateRef<ListboxHeaderTemplateContext<any>> | Custom header template.               |
| filter      | TemplateRef<ListboxFilterTemplateContext>      | Custom filter template.               |
| footer      | TemplateRef<ListboxFooterTemplateContext<any>> | Custom footer template.               |
| emptyfilter | TemplateRef<void>                              | Custom empty filter message template. |
| empty       | TemplateRef<void>                              | Custom empty message template.        |
| filtericon  | TemplateRef<void>                              | Custom filter icon template.          |
| checkicon   | TemplateRef<ListboxCheckIconTemplateContext>   | Custom check icon template.           |
| checkmark   | TemplateRef<ListboxCheckmarkTemplateContext>   | Custom checkmark icon template.       |
| loader      | TemplateRef<ListboxLoaderTemplateContext>      | Custom loader template.               |

## Methods

| Name        | Parameters             | Return Type | Description              |
| ----------- | ---------------------- | ----------- | ------------------------ |
| updateModel | value: any, event: any | void        | Updates the model value. |

**Full API & more examples:** https://primeng.org/listbox
