# Select (`p-select`)

Select is used to choose an item from a collection of options.

**Import:**

```ts
import { SelectModule } from "primeng/select";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { SelectModule } from "primeng/select";

interface City {
  name: string;
  code: string;
}

@Component({
  template: `
    <div class="card flex justify-center">
      <p-select
        [options]="cities"
        [(ngModel)]="selectedCity"
        optionLabel="name"
        placeholder="Select a City"
        class="w-full md:w-56"
      />
    </div>
  `,
  standalone: true,
  imports: [SelectModule, FormsModule],
})
export class SelectBasicDemo implements OnInit {
  cities: City[];
  selectedCity: City | undefined;

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

| Name                  | Type                                                                                                          | Default    | Description                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required              | InputSignalWithTransform<boolean, unknown>                                                                    | false      | There must be a value (if set).                                                                                                                                                                                                                      |
| invalid               | InputSignalWithTransform<boolean, unknown>                                                                    | false      | When present, it specifies that the component should have invalid state style.                                                                                                                                                                       |
| disabled              | InputSignalWithTransform<boolean, unknown>                                                                    | false      | When present, it specifies that the component should have disabled state style.                                                                                                                                                                      |
| name                  | InputSignal<string>                                                                                           | undefined  | When present, it specifies that the name of the input.                                                                                                                                                                                               |
| fluid                 | InputSignalWithTransform<boolean, unknown>                                                                    | false      | Spans 100% width of the container when enabled.                                                                                                                                                                                                      |
| variant               | InputSignal<"outlined" \| "filled">                                                                           | 'outlined' | Specifies the input variant of the component.                                                                                                                                                                                                        |
| size                  | InputSignal<"small" \| "large">                                                                               | undefined  | Specifies the size of the component.                                                                                                                                                                                                                 |
| inputSize             | InputSignal<number>                                                                                           | undefined  | Specifies the visible width of the input element in characters.                                                                                                                                                                                      |
| pattern               | InputSignal<string>                                                                                           | undefined  | Specifies the value must match the pattern.                                                                                                                                                                                                          |
| min                   | InputSignal<number>                                                                                           | undefined  | The value must be greater than or equal to the value.                                                                                                                                                                                                |
| max                   | InputSignal<number>                                                                                           | undefined  | The value must be less than or equal to the value.                                                                                                                                                                                                   |
| step                  | InputSignal<number>                                                                                           | undefined  | Unless the step is set to the any literal, the value must be min + an integral multiple of the step.                                                                                                                                                 |
| minlength             | InputSignal<number>                                                                                           | undefined  | The number of characters (code points) must not be less than the value of the attribute, if non-empty.                                                                                                                                               |
| maxlength             | InputSignal<number>                                                                                           | undefined  | The number of characters (code points) must not exceed the value of the attribute.                                                                                                                                                                   |
| id                    | string                                                                                                        | -          | Unique identifier of the component                                                                                                                                                                                                                   |
| scrollHeight          | string                                                                                                        | 200px      | Height of the viewport in pixels, a scrollbar is defined if height of list exceeds this value.                                                                                                                                                       |
| filter                | boolean                                                                                                       | false      | When specified, displays an input field to filter the items on keyup.                                                                                                                                                                                |
| panelStyle            | { [klass: string]: any }                                                                                      | -          | Inline style of the overlay panel element.                                                                                                                                                                                                           |
| panelStyleClass       | string                                                                                                        | -          | Style class of the overlay panel element.                                                                                                                                                                                                            |
| readonly              | boolean                                                                                                       | false      | When present, it specifies that the component cannot be edited.                                                                                                                                                                                      |
| editable              | boolean                                                                                                       | false      | When present, custom value instead of predefined options can be entered using the editable input field.                                                                                                                                              |
| tabindex              | number                                                                                                        | 0          | Index of the element in tabbing order.                                                                                                                                                                                                               |
| placeholder           | Signal<string>                                                                                                | -          | Default text to display when no option is selected.                                                                                                                                                                                                  |
| loadingIcon           | string                                                                                                        | -          | Icon to display in loading state.                                                                                                                                                                                                                    |
| filterPlaceholder     | string                                                                                                        | -          | Placeholder text to show when filter input is empty.                                                                                                                                                                                                 |
| filterLocale          | string                                                                                                        | -          | Locale to use in filtering. The default locale is the host environment's current locale.                                                                                                                                                             |
| inputId               | string                                                                                                        | -          | Identifier of the accessible input element.                                                                                                                                                                                                          |
| dataKey               | string                                                                                                        | -          | A property to uniquely identify a value in options.                                                                                                                                                                                                  |
| filterBy              | string                                                                                                        | -          | When filtering is enabled, filterBy decides which field or fields (comma separated) to search against.                                                                                                                                               |
| filterFields          | any[]                                                                                                         | -          | Fields used when filtering the options, defaults to optionLabel.                                                                                                                                                                                     |
| autofocus             | boolean                                                                                                       | false      | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                |
| resetFilterOnHide     | boolean                                                                                                       | false      | Clears the filter value when hiding the select.                                                                                                                                                                                                      |
| checkmark             | boolean                                                                                                       | false      | Whether the selected option will be shown with a check mark.                                                                                                                                                                                         |
| dropdownIcon          | string                                                                                                        | -          | Icon class of the select icon.                                                                                                                                                                                                                       |
| loading               | boolean                                                                                                       | false      | Whether the select is in loading state.                                                                                                                                                                                                              |
| optionLabel           | string                                                                                                        | -          | Name of the label field of an option.                                                                                                                                                                                                                |
| optionValue           | string                                                                                                        | -          | Name of the value field of an option.                                                                                                                                                                                                                |
| optionDisabled        | string                                                                                                        | -          | Name of the disabled field of an option.                                                                                                                                                                                                             |
| optionGroupLabel      | string                                                                                                        | label      | Name of the label field of an option group.                                                                                                                                                                                                          |
| optionGroupChildren   | string                                                                                                        | items      | Name of the options field of an option group.                                                                                                                                                                                                        |
| group                 | boolean                                                                                                       | false      | Whether to display options as grouped when nested options are provided.                                                                                                                                                                              |
| showClear             | boolean                                                                                                       | false      | When enabled, a clear icon is displayed to clear the value.                                                                                                                                                                                          |
| emptyFilterMessage    | string                                                                                                        | -          | Text to display when filtering does not return any results. Defaults to global value in i18n translation configuration.                                                                                                                              |
| emptyMessage          | string                                                                                                        | -          | Text to display when there is no data. Defaults to global value in i18n translation configuration.                                                                                                                                                   |
| lazy                  | boolean                                                                                                       | false      | Defines if data is loaded and interacted with in lazy manner.                                                                                                                                                                                        |
| virtualScroll         | boolean                                                                                                       | false      | Whether the data should be loaded on demand during scroll.                                                                                                                                                                                           |
| virtualScrollItemSize | number                                                                                                        | -          | Height of an item in the list for VirtualScrolling.                                                                                                                                                                                                  |
| virtualScrollOptions  | ScrollerOptions                                                                                               | -          | Whether to use the scroller feature. The properties of scroller component can be used like an object in it.                                                                                                                                          |
| overlayOptions        | OverlayOptions                                                                                                | -          | Whether to use overlay API feature. The properties of overlay API can be used like an object in it.                                                                                                                                                  |
| ariaFilterLabel       | string                                                                                                        | -          | Defines a string that labels the filter input.                                                                                                                                                                                                       |
| ariaLabel             | string                                                                                                        | -          | Used to define a aria label attribute the current element.                                                                                                                                                                                           |
| ariaLabelledBy        | string                                                                                                        | -          | Establishes relationships between the component and label(s) where its value should be one or more element IDs.                                                                                                                                      |
| filterMatchMode       | "startsWith" \| "contains" \| "endsWith" \| "equals" \| "notEquals" \| "in" \| "lt" \| "lte" \| "gt" \| "gte" | contains   | Defines how the items are filtered.                                                                                                                                                                                                                  |
| tooltip               | string                                                                                                        | -          | Advisory information to display in a tooltip on hover.                                                                                                                                                                                               |
| tooltipPosition       | "right" \| "left" \| "top" \| "bottom"                                                                        | right      | Position of the tooltip.                                                                                                                                                                                                                             |
| tooltipPositionStyle  | string                                                                                                        | absolute   | Type of CSS position.                                                                                                                                                                                                                                |
| tooltipStyleClass     | string                                                                                                        | -          | Style class of the tooltip.                                                                                                                                                                                                                          |
| focusOnHover          | boolean                                                                                                       | true       | Fields used when filtering the options, defaults to optionLabel.                                                                                                                                                                                     |
| selectOnFocus         | boolean                                                                                                       | false      | Determines if the option will be selected on focus.                                                                                                                                                                                                  |
| autoOptionFocus       | boolean                                                                                                       | false      | Whether to focus on the first visible or selected element when the overlay panel is shown.                                                                                                                                                           |
| autofocusFilter       | boolean                                                                                                       | true       | Applies focus to the filter element when the overlay is shown.                                                                                                                                                                                       |
| filterValue           | string                                                                                                        | -          | When specified, filter displays with this value.                                                                                                                                                                                                     |
| options               | any[]                                                                                                         | -          | An array of objects to display as the available options.                                                                                                                                                                                             |
| appendTo              | InputSignal<any>                                                                                              | 'self'     | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions         | InputSignal<MotionOptions>                                                                                    | ...        | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name       | Parameters                 | Description                                          |
| ---------- | -------------------------- | ---------------------------------------------------- |
| onChange   | event: SelectChangeEvent   | Callback to invoke when value of select changes.     |
| onFilter   | event: SelectFilterEvent   | Callback to invoke when data is filtered.            |
| onFocus    | event: Event               | Callback to invoke when select gets focus.           |
| onBlur     | event: Event               | Callback to invoke when select loses focus.          |
| onClick    | event: MouseEvent          | Callback to invoke when component is clicked.        |
| onShow     | event: AnimationEvent      | Callback to invoke when select overlay gets visible. |
| onHide     | event: AnimationEvent      | Callback to invoke when select overlay gets hidden.  |
| onClear    | event: Event               | Callback to invoke when select clears the value.     |
| onLazyLoad | event: SelectLazyLoadEvent | Callback to invoke in lazy mode to load new data.    |

## Templates

| Name         | Type                                                | Description                    |
| ------------ | --------------------------------------------------- | ------------------------------ |
| item         | TemplateRef<SelectItemTemplateContext<any>>         | Custom item template.          |
| group        | TemplateRef<SelectGroupTemplateContext<any>>        | Custom group template.         |
| loader       | TemplateRef<SelectLoaderTemplateContext>            | Custom loader template.        |
| selecteditem | TemplateRef<SelectSelectedItemTemplateContext<any>> | Custom selected item template. |
| header       | TemplateRef<void>                                   | Custom header template.        |
| filter       | TemplateRef<SelectFilterTemplateContext>            | Custom filter template.        |
| footer       | TemplateRef<void>                                   | Custom footer template.        |
| emptyfilter  | TemplateRef<void>                                   | Custom empty filter template.  |
| empty        | TemplateRef<void>                                   | Custom empty template.         |
| dropdownicon | TemplateRef<SelectIconTemplateContext>              | Custom dropdown icon template. |
| loadingicon  | TemplateRef<void>                                   | Custom loading icon template.  |
| clearicon    | TemplateRef<SelectIconTemplateContext>              | Custom clear icon template.    |
| filtericon   | TemplateRef<void>                                   | Custom filter icon template.   |
| onicon       | TemplateRef<void>                                   | Custom on icon template.       |
| officon      | TemplateRef<void>                                   | Custom off icon template.      |
| cancelicon   | TemplateRef<void>                                   | Custom cancel icon template.   |

## Methods

| Name        | Parameters   | Return Type | Description                         |
| ----------- | ------------ | ----------- | ----------------------------------- |
| resetFilter |              | void        | Callback to invoke on filter reset. |
| show        | isFocus: any | void        | Displays the panel.                 |
| hide        | isFocus: any | void        | Hides the panel.                    |
| focus       |              | void        | Applies focus.                      |
| clear       | event: Event | void        | Clears the model.                   |

**Full API & more examples:** https://primeng.org/select
