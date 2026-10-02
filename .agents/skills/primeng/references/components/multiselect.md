# MultiSelect (`p-multiselect`)

MultiSelect is used to select multiple items from a collection.

**Import:**

```ts
import { MultiSelectModule } from "primeng/multiselect";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { MultiSelectModule } from "primeng/multiselect";

interface City {
  name: string;
  code: string;
}

@Component({
  template: `
    <div class="card flex justify-center">
      <p-multiselect
        [options]="cities"
        [(ngModel)]="selectedCities"
        optionLabel="name"
        placeholder="Select Cities"
        [maxSelectedLabels]="3"
        class="w-full md:w-80"
      />
    </div>
  `,
  standalone: true,
  imports: [MultiSelectModule, FormsModule],
})
export class MultiselectBasicDemo implements OnInit {
  cities!: City[];
  selectedCities!: any[];

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

| Name                  | Type                                                                                                          | Default   | Description                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required              | InputSignalWithTransform<boolean, unknown>                                                                    | false     | There must be a value (if set).                                                                                                                                                                                                                      |
| invalid               | InputSignalWithTransform<boolean, unknown>                                                                    | false     | When present, it specifies that the component should have invalid state style.                                                                                                                                                                       |
| disabled              | InputSignalWithTransform<boolean, unknown>                                                                    | false     | When present, it specifies that the component should have disabled state style.                                                                                                                                                                      |
| name                  | InputSignal<string>                                                                                           | undefined | When present, it specifies that the name of the input.                                                                                                                                                                                               |
| id                    | string                                                                                                        | -         | Unique identifier of the component                                                                                                                                                                                                                   |
| ariaLabel             | string                                                                                                        | -         | Defines a string that labels the input for accessibility.                                                                                                                                                                                            |
| panelStyle            | any                                                                                                           | -         | Inline style of the overlay panel.                                                                                                                                                                                                                   |
| panelStyleClass       | string                                                                                                        | -         | Style class of the overlay panel element.                                                                                                                                                                                                            |
| inputId               | string                                                                                                        | -         | Identifier of the focus input to match a label defined for the component.                                                                                                                                                                            |
| readonly              | boolean                                                                                                       | false     | When present, it specifies that the component cannot be edited.                                                                                                                                                                                      |
| group                 | boolean                                                                                                       | false     | Whether to display options as grouped when nested options are provided.                                                                                                                                                                              |
| filter                | boolean                                                                                                       | true      | When specified, displays an input field to filter the items on keyup.                                                                                                                                                                                |
| filterPlaceHolder     | string                                                                                                        | -         | Defines placeholder of the filter input.                                                                                                                                                                                                             |
| filterLocale          | string                                                                                                        | -         | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                             |
| overlayVisible        | boolean                                                                                                       | false     | Specifies the visibility of the options panel.                                                                                                                                                                                                       |
| tabindex              | number                                                                                                        | 0         | Index of the element in tabbing order.                                                                                                                                                                                                               |
| dataKey               | string                                                                                                        | -         | A property to uniquely identify a value in options.                                                                                                                                                                                                  |
| ariaLabelledBy        | string                                                                                                        | -         | Establishes relationships between the component and label(s) where its value should be one or more element IDs.                                                                                                                                      |
| displaySelectedLabel  | boolean                                                                                                       | -         | Whether to show labels of selected item labels or use default label.                                                                                                                                                                                 |
| maxSelectedLabels     | number                                                                                                        | -         | Decides how many selected item labels to show at most.                                                                                                                                                                                               |
| selectionLimit        | number                                                                                                        | -         | Maximum number of selectable items.                                                                                                                                                                                                                  |
| selectedItemsLabel    | string                                                                                                        | -         | Label to display after exceeding max selected labels e.g. ({0} items selected), defaults "ellipsis" keyword to indicate a text-overflow.                                                                                                             |
| showToggleAll         | boolean                                                                                                       | true      | Whether to show the checkbox at header to toggle all items at once.                                                                                                                                                                                  |
| emptyFilterMessage    | string                                                                                                        | -         | Text to display when filtering does not return any results.                                                                                                                                                                                          |
| emptyMessage          | string                                                                                                        | -         | Text to display when there is no data. Defaults to global value in i18n translation configuration.                                                                                                                                                   |
| resetFilterOnHide     | boolean                                                                                                       | false     | Clears the filter value when hiding the dropdown.                                                                                                                                                                                                    |
| dropdownIcon          | string                                                                                                        | -         | Icon class of the dropdown icon.                                                                                                                                                                                                                     |
| chipIcon              | string                                                                                                        | -         | Icon class of the chip icon.                                                                                                                                                                                                                         |
| optionLabel           | string                                                                                                        | -         | Name of the label field of an option.                                                                                                                                                                                                                |
| optionValue           | string                                                                                                        | -         | Name of the value field of an option.                                                                                                                                                                                                                |
| optionDisabled        | string                                                                                                        | -         | Name of the disabled field of an option.                                                                                                                                                                                                             |
| optionGroupLabel      | string                                                                                                        | label     | Name of the label field of an option group.                                                                                                                                                                                                          |
| optionGroupChildren   | string                                                                                                        | items     | Name of the options field of an option group.                                                                                                                                                                                                        |
| showHeader            | boolean                                                                                                       | true      | Whether to show the header.                                                                                                                                                                                                                          |
| filterBy              | string                                                                                                        | -         | When filtering is enabled, filterBy decides which field or fields (comma separated) to search against.                                                                                                                                               |
| scrollHeight          | string                                                                                                        | 200px     | Height of the viewport in pixels, a scrollbar is defined if height of list exceeds this value.                                                                                                                                                       |
| lazy                  | boolean                                                                                                       | false     | Defines if data is loaded and interacted with in lazy manner.                                                                                                                                                                                        |
| virtualScroll         | boolean                                                                                                       | false     | Whether the data should be loaded on demand during scroll.                                                                                                                                                                                           |
| loading               | boolean                                                                                                       | false     | Whether the multiselect is in loading state.                                                                                                                                                                                                         |
| virtualScrollItemSize | number                                                                                                        | -         | Height of an item in the list for VirtualScrolling.                                                                                                                                                                                                  |
| loadingIcon           | string                                                                                                        | -         | Icon to display in loading state.                                                                                                                                                                                                                    |
| virtualScrollOptions  | ScrollerOptions                                                                                               | -         | Whether to use the scroller feature. The properties of scroller component can be used like an object in it.                                                                                                                                          |
| overlayOptions        | OverlayOptions                                                                                                | -         | Whether to use overlay API feature. The properties of overlay API can be used like an object in it.                                                                                                                                                  |
| ariaFilterLabel       | string                                                                                                        | -         | Defines a string that labels the filter input.                                                                                                                                                                                                       |
| filterMatchMode       | "startsWith" \| "contains" \| "endsWith" \| "equals" \| "notEquals" \| "in" \| "lt" \| "lte" \| "gt" \| "gte" | contains  | Defines how the items are filtered.                                                                                                                                                                                                                  |
| tooltip               | string                                                                                                        | -         | Advisory information to display in a tooltip on hover.                                                                                                                                                                                               |
| tooltipPosition       | "right" \| "left" \| "top" \| "bottom"                                                                        | right     | Position of the tooltip.                                                                                                                                                                                                                             |
| tooltipPositionStyle  | string                                                                                                        | absolute  | Type of CSS position.                                                                                                                                                                                                                                |
| tooltipStyleClass     | string                                                                                                        | -         | Style class of the tooltip.                                                                                                                                                                                                                          |
| autofocusFilter       | boolean                                                                                                       | false     | Applies focus to the filter element when the overlay is shown.                                                                                                                                                                                       |
| display               | string                                                                                                        | comma     | Defines how the selected items are displayed.                                                                                                                                                                                                        |
| autocomplete          | string                                                                                                        | off       | Defines the autocomplete is active.                                                                                                                                                                                                                  |
| showClear             | boolean                                                                                                       | false     | When enabled, a clear icon is displayed to clear the value.                                                                                                                                                                                          |
| autofocus             | boolean                                                                                                       | false     | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                |
| placeholder           | Signal<string>                                                                                                | -         | Label to display when there are no selections.                                                                                                                                                                                                       |
| options               | any[]                                                                                                         | -         | An array of objects to display as the available options.                                                                                                                                                                                             |
| filterValue           | string                                                                                                        | -         | When specified, filter displays with this value.                                                                                                                                                                                                     |
| selectAll             | boolean                                                                                                       | -         | Whether all data is selected.                                                                                                                                                                                                                        |
| focusOnHover          | boolean                                                                                                       | true      | Indicates whether to focus on options when hovering over them, defaults to optionLabel.                                                                                                                                                              |
| filterFields          | any[]                                                                                                         | -         | Fields used when filtering the options, defaults to optionLabel.                                                                                                                                                                                     |
| selectOnFocus         | boolean                                                                                                       | false     | Determines if the option will be selected on focus.                                                                                                                                                                                                  |
| autoOptionFocus       | boolean                                                                                                       | false     | Whether to focus on the first visible or selected element when the overlay panel is shown.                                                                                                                                                           |
| highlightOnSelect     | boolean                                                                                                       | true      | Whether the selected option will be add highlight class.                                                                                                                                                                                             |
| size                  | InputSignal<"small" \| "large">                                                                               | undefined | Specifies the size of the component.                                                                                                                                                                                                                 |
| variant               | InputSignal<"outlined" \| "filled">                                                                           | undefined | Specifies the input variant of the component.                                                                                                                                                                                                        |
| fluid                 | InputSignalWithTransform<boolean, unknown>                                                                    | undefined | Spans 100% width of the container when enabled.                                                                                                                                                                                                      |
| appendTo              | InputSignal<any>                                                                                              | 'self'    | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions         | InputSignal<MotionOptions>                                                                                    | ...       | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name              | Parameters                             | Description                                            |
| ----------------- | -------------------------------------- | ------------------------------------------------------ |
| onChange          | event: MultiSelectChangeEvent          | Callback to invoke when value changes.                 |
| onFilter          | event: MultiSelectFilterEvent          | Callback to invoke when data is filtered.              |
| onFocus           | event: MultiSelectFocusEvent           | Callback to invoke when multiselect receives focus.    |
| onBlur            | event: MultiSelectBlurEvent            | Callback to invoke when multiselect loses focus.       |
| onClick           | event: Event                           | Callback to invoke when component is clicked.          |
| onClear           | value: void                            | Callback to invoke when input field is cleared.        |
| onPanelShow       | event: AnimationEvent                  | Callback to invoke when overlay panel becomes visible. |
| onPanelHide       | event: AnimationEvent                  | Callback to invoke when overlay panel becomes hidden.  |
| onLazyLoad        | event: MultiSelectLazyLoadEvent        | Callback to invoke in lazy mode to load new data.      |
| onRemove          | event: MultiSelectRemoveEvent          | Callback to invoke in lazy mode to load new data.      |
| onSelectAllChange | event: MultiSelectSelectAllChangeEvent | Callback to invoke when all data is selected.          |

## Templates

| Name               | Type                                                      | Description                           |
| ------------------ | --------------------------------------------------------- | ------------------------------------- |
| item               | TemplateRef<MultiSelectItemTemplateContext<any>>          | Custom item template.                 |
| group              | TemplateRef<MultiSelectGroupTemplateContext<any>>         | Custom group template.                |
| loader             | TemplateRef<MultiSelectLoaderTemplateContext>             | Custom loader template.               |
| header             | TemplateRef<void>                                         | Custom header template.               |
| filter             | TemplateRef<MultiSelectFilterTemplateContext>             | Custom filter template.               |
| footer             | TemplateRef<void>                                         | Custom footer template.               |
| emptyfilter        | TemplateRef<void>                                         | Custom empty filter template.         |
| empty              | TemplateRef<void>                                         | Custom empty template.                |
| selecteditems      | TemplateRef<MultiSelectSelectedItemsTemplateContext<any>> | Custom selected items template.       |
| loadingicon        | TemplateRef<void>                                         | Custom loading icon template.         |
| filtericon         | TemplateRef<void>                                         | Custom filter icon template.          |
| removetokenicon    | TemplateRef<MultiSelectChipIconTemplateContext>           | Custom remove token icon template.    |
| chipicon           | TemplateRef<MultiSelectChipIconTemplateContext>           | Custom chip icon template.            |
| clearicon          | TemplateRef<void>                                         | Custom clear icon template.           |
| dropdownicon       | TemplateRef<MultiSelectDropdownIconTemplateContext>       | Custom dropdown icon template.        |
| itemcheckboxicon   | TemplateRef<MultiSelectItemCheckboxIconTemplateContext>   | Custom item checkbox icon template.   |
| headercheckboxicon | TemplateRef<MultiSelectHeaderCheckboxIconTemplateContext> | Custom header checkbox icon template. |

## Methods

| Name        | Parameters             | Return Type | Description              |
| ----------- | ---------------------- | ----------- | ------------------------ |
| updateModel | value: any, event: any | void        | Updates the model value. |
| show        | isFocus: any           | void        | Displays the panel.      |
| hide        | isFocus: any           | void        | Hides the panel.         |

**Full API & more examples:** https://primeng.org/multiselect
