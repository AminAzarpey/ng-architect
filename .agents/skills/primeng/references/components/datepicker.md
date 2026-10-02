# DatePicker (`p-datepicker`)

DatePicker is an input component to select a date.

**Import:**

```ts
import { DatePickerModule } from "primeng/datepicker";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { DatePickerModule } from "primeng/datepicker";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-datepicker [(ngModel)]="date" />
    </div>
  `,
  standalone: true,
  imports: [DatePickerModule, FormsModule],
})
export class DatepickerBasicDemo {
  date: Date | undefined;
}
```

## Inputs

| Name                        | Type                                       | Default    | Description                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required                    | InputSignalWithTransform<boolean, unknown> | false      | There must be a value (if set).                                                                                                                                                                                                                      |
| invalid                     | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have invalid state style.                                                                                                                                                                       |
| disabled                    | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have disabled state style.                                                                                                                                                                      |
| name                        | InputSignal<string>                        | undefined  | When present, it specifies that the name of the input.                                                                                                                                                                                               |
| fluid                       | InputSignalWithTransform<boolean, unknown> | false      | Spans 100% width of the container when enabled.                                                                                                                                                                                                      |
| variant                     | InputSignal<"outlined" \| "filled">        | 'outlined' | Specifies the input variant of the component.                                                                                                                                                                                                        |
| size                        | InputSignal<"small" \| "large">            | undefined  | Specifies the size of the component.                                                                                                                                                                                                                 |
| inputSize                   | InputSignal<number>                        | undefined  | Specifies the visible width of the input element in characters.                                                                                                                                                                                      |
| pattern                     | InputSignal<string>                        | undefined  | Specifies the value must match the pattern.                                                                                                                                                                                                          |
| min                         | InputSignal<number>                        | undefined  | The value must be greater than or equal to the value.                                                                                                                                                                                                |
| max                         | InputSignal<number>                        | undefined  | The value must be less than or equal to the value.                                                                                                                                                                                                   |
| step                        | InputSignal<number>                        | undefined  | Unless the step is set to the any literal, the value must be min + an integral multiple of the step.                                                                                                                                                 |
| minlength                   | InputSignal<number>                        | undefined  | The number of characters (code points) must not be less than the value of the attribute, if non-empty.                                                                                                                                               |
| maxlength                   | InputSignal<number>                        | undefined  | The number of characters (code points) must not exceed the value of the attribute.                                                                                                                                                                   |
| inputStyle                  | { [klass: string]: any }                   | -          | Inline style of the input field.                                                                                                                                                                                                                     |
| inputId                     | string                                     | -          | Identifier of the focus input to match a label defined for the component.                                                                                                                                                                            |
| inputStyleClass             | string                                     | -          | Style class of the input field.                                                                                                                                                                                                                      |
| placeholder                 | string                                     | -          | Placeholder text for the input.                                                                                                                                                                                                                      |
| ariaLabelledBy              | string                                     | -          | Establishes relationships between the component and label(s) where its value should be one or more element IDs.                                                                                                                                      |
| ariaLabel                   | string                                     | -          | Defines a string that labels the input for accessibility.                                                                                                                                                                                            |
| iconAriaLabel               | string                                     | -          | Defines a string that labels the icon button for accessibility.                                                                                                                                                                                      |
| dateFormat                  | string                                     | -          | Format of the date which can also be defined at locale settings.                                                                                                                                                                                     |
| multipleSeparator           | string                                     | ,          | Separator for multiple selection mode.                                                                                                                                                                                                               |
| rangeSeparator              | string                                     | -          | Separator for joining start and end dates on range selection mode.                                                                                                                                                                                   |
| inline                      | boolean                                    | false      | When enabled, displays the datepicker as inline. Default is false for popup mode.                                                                                                                                                                    |
| showOtherMonths             | boolean                                    | true       | Whether to display dates in other months (non-selectable) at the start or end of the current month. To make these days selectable use the selectOtherMonths option.                                                                                  |
| selectOtherMonths           | boolean                                    | false      | Whether days in other months shown before or after the current month are selectable. This only applies if the showOtherMonths option is set to true.                                                                                                 |
| showIcon                    | boolean                                    | false      | When enabled, displays a button with icon next to input.                                                                                                                                                                                             |
| icon                        | string                                     | -          | Icon of the datepicker button.                                                                                                                                                                                                                       |
| readonlyInput               | boolean                                    | false      | When specified, prevents entering the date manually with keyboard.                                                                                                                                                                                   |
| shortYearCutoff             | any                                        | +10        | The cutoff year for determining the century for a date.                                                                                                                                                                                              |
| hourFormat                  | string                                     | -          | Specifies 12 or 24 hour format.                                                                                                                                                                                                                      |
| timeOnly                    | boolean                                    | false      | Whether to display timepicker only.                                                                                                                                                                                                                  |
| stepHour                    | number                                     | 1          | Hours to change per step.                                                                                                                                                                                                                            |
| stepMinute                  | number                                     | 1          | Minutes to change per step.                                                                                                                                                                                                                          |
| stepSecond                  | number                                     | 1          | Seconds to change per step.                                                                                                                                                                                                                          |
| showSeconds                 | boolean                                    | false      | Whether to show the seconds in time picker.                                                                                                                                                                                                          |
| showOnFocus                 | boolean                                    | true       | When disabled, datepicker will not be visible with input focus.                                                                                                                                                                                      |
| showWeek                    | boolean                                    | false      | When enabled, datepicker will show week numbers.                                                                                                                                                                                                     |
| startWeekFromFirstDayOfYear | boolean                                    | false      | When enabled, datepicker will start week numbers from first day of the year.                                                                                                                                                                         |
| showClear                   | boolean                                    | false      | When enabled, a clear icon is displayed to clear the value.                                                                                                                                                                                          |
| dataType                    | string                                     | date       | Type of the value to write back to ngModel, default is date and alternative is string.                                                                                                                                                               |
| selectionMode               | "multiple" \| "single" \| "range"          | single     | Defines the quantity of the selection, valid values are "single", "multiple" and "range".                                                                                                                                                            |
| maxDateCount                | number                                     | -          | Maximum number of selectable dates in multiple mode.                                                                                                                                                                                                 |
| showButtonBar               | boolean                                    | false      | Whether to display today and clear buttons at the footer                                                                                                                                                                                             |
| todayButtonStyleClass       | string                                     | -          | Style class of the today button.                                                                                                                                                                                                                     |
| clearButtonStyleClass       | string                                     | -          | Style class of the clear button.                                                                                                                                                                                                                     |
| autofocus                   | boolean                                    | false      | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                |
| autoZIndex                  | boolean                                    | true       | Whether to automatically manage layering.                                                                                                                                                                                                            |
| baseZIndex                  | number                                     | 0          | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| panelStyleClass             | string                                     | -          | Style class of the datetimepicker container element.                                                                                                                                                                                                 |
| panelStyle                  | any                                        | -          | Inline style of the datetimepicker container element.                                                                                                                                                                                                |
| keepInvalid                 | boolean                                    | false      | Keep invalid value when input blur.                                                                                                                                                                                                                  |
| hideOnDateTimeSelect        | boolean                                    | true       | Whether to hide the overlay on date selection.                                                                                                                                                                                                       |
| touchUI                     | boolean                                    | false      | When enabled, datepicker overlay is displayed as optimized for touch devices.                                                                                                                                                                        |
| timeSeparator               | string                                     | :          | Separator of time selector.                                                                                                                                                                                                                          |
| focusTrap                   | boolean                                    | true       | When enabled, can only focus on elements inside the datepicker.                                                                                                                                                                                      |
| tabindex                    | number                                     | -          | Index of the element in tabbing order.                                                                                                                                                                                                               |
| minDate                     | Date                                       | -          | The minimum selectable date.                                                                                                                                                                                                                         |
| maxDate                     | Date                                       | -          | The maximum selectable date.                                                                                                                                                                                                                         |
| disabledDates               | Date[]                                     | -          | Array with dates that should be disabled (not selectable).                                                                                                                                                                                           |
| disabledDays                | number[]                                   | -          | Array with weekday numbers that should be disabled (not selectable).                                                                                                                                                                                 |
| showTime                    | boolean                                    | -          | Whether to display timepicker.                                                                                                                                                                                                                       |
| responsiveOptions           | DatePickerResponsiveOptions[]              | -          | An array of options for responsive design.                                                                                                                                                                                                           |
| numberOfMonths              | number                                     | -          | Number of months to display.                                                                                                                                                                                                                         |
| firstDayOfWeek              | number                                     | -          | Defines the first of the week for various date calculations.                                                                                                                                                                                         |
| view                        | DatePickerTypeView                         | -          | Type of view to display, valid values are "date" for datepicker and "month" for month picker.                                                                                                                                                        |
| defaultDate                 | Date                                       | -          | Set the date to highlight on first opening if the field is blank.                                                                                                                                                                                    |
| appendTo                    | InputSignal<any>                           | 'self'     | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| motionOptions               | InputSignal<MotionOptions>                 | ...        | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name           | Parameters                        | Description                                                      |
| -------------- | --------------------------------- | ---------------------------------------------------------------- |
| onFocus        | event: Event                      | Callback to invoke on focus of input field.                      |
| onBlur         | event: Event                      | Callback to invoke on blur of input field.                       |
| onClose        | value: HTMLElement                | Callback to invoke when date panel closed.                       |
| onSelect       | value: Date                       | Callback to invoke on date select.                               |
| onClear        | value: any                        | Callback to invoke when input field cleared.                     |
| onInput        | value: any                        | Callback to invoke when input field is being typed.              |
| onTodayClick   | value: Date                       | Callback to invoke when today button is clicked.                 |
| onClearClick   | value: any                        | Callback to invoke when clear button is clicked.                 |
| onMonthChange  | event: DatePickerMonthChangeEvent | Callback to invoke when a month is changed using the navigators. |
| onYearChange   | event: DatePickerYearChangeEvent  | Callback to invoke when a year is changed using the navigators.  |
| onClickOutside | value: any                        | Callback to invoke when clicked outside of the date panel.       |
| onShow         | value: HTMLElement                | Callback to invoke when datepicker panel is shown.               |

## Templates

| Name          | Type                                               | Description                              |
| ------------- | -------------------------------------------------- | ---------------------------------------- |
| date          | TemplateRef<DatePickerDateTemplateContext>         | Custom template for date cells.          |
| header        | TemplateRef<void>                                  | Custom template for header section.      |
| footer        | TemplateRef<void>                                  | Custom template for footer section.      |
| disableddate  | TemplateRef<DatePickerDisabledDateTemplateContext> | Custom template for disabled date cells. |
| decade        | TemplateRef<DatePickerDecadeTemplateContext>       | Custom template for decade view.         |
| previousicon  | TemplateRef<void>                                  | Custom template for previous month icon. |
| nexticon      | TemplateRef<void>                                  | Custom template for next month icon.     |
| triggericon   | TemplateRef<void>                                  | Custom template for trigger icon.        |
| clearicon     | TemplateRef<void>                                  | Custom template for clear icon.          |
| decrementicon | TemplateRef<void>                                  | Custom template for decrement icon.      |
| incrementicon | TemplateRef<void>                                  | Custom template for increment icon.      |
| inputicon     | TemplateRef<DatePickerInputIconTemplateContext>    | Custom template for input icon.          |
| buttonbar     | TemplateRef<DatePickerButtonBarTemplateContext>    | Custom template for button bar.          |

**Full API & more examples:** https://primeng.org/datepicker
