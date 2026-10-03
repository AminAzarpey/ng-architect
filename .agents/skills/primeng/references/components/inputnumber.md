# InputNumber (`p-inputnumber`)

InputNumber is an input component to provide numerical input.

**Import:**

```ts
import { InputNumberModule } from "primeng/inputnumber";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { InputNumberModule } from "primeng/inputnumber";

@Component({
  template: `
    <p-fluid class="card flex flex-wrap gap-4">
      <div class="flex-auto">
        <label class="mb-2 block font-bold" for="stacked">Stacked</label>
        <p-inputnumber
          [(ngModel)]="value1"
          [showButtons]="true"
          inputId="stacked"
          mode="currency"
          currency="USD"
        />
      </div>
      <div class="flex-auto">
        <label class="mb-2 block font-bold" for="minmax-buttons"
          >Min-Max Boundaries</label
        >
        <p-inputnumber
          [(ngModel)]="value2"
          mode="decimal"
          [showButtons]="true"
          inputId="minmax-buttons"
          [min]="0"
          [max]="100"
        />
      </div>
      <div class="flex-auto">
        <label class="mb-2 block font-bold" for="horizontal"
          >Horizontal with Step</label
        >
        <p-inputnumber
          [(ngModel)]="value3"
          [showButtons]="true"
          buttonLayout="horizontal"
          inputId="horizontal"
          spinnerMode="horizontal"
          [step]="0.25"
          mode="currency"
          currency="EUR"
        >
          <ng-template #incrementbuttonicon>
            <span class="pi pi-plus"></span>
          </ng-template>
          <ng-template #decrementbuttonicon>
            <span class="pi pi-minus"></span>
          </ng-template>
        </p-inputnumber>
      </div>
    </p-fluid>
  `,
  standalone: true,
  imports: [InputNumberModule, FormsModule],
})
export class InputnumberButtonsDemo {
  value1: number = 20;
  value2: number = 10.5;
  value3: number = 25;
}
```

## Inputs

| Name                 | Type                                       | Default    | Description                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required             | InputSignalWithTransform<boolean, unknown> | false      | There must be a value (if set).                                                                                                                                                                                                                                                                                                                                                    |
| invalid              | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have invalid state style.                                                                                                                                                                                                                                                                                                     |
| disabled             | InputSignalWithTransform<boolean, unknown> | false      | When present, it specifies that the component should have disabled state style.                                                                                                                                                                                                                                                                                                    |
| name                 | InputSignal<string>                        | undefined  | When present, it specifies that the name of the input.                                                                                                                                                                                                                                                                                                                             |
| fluid                | InputSignalWithTransform<boolean, unknown> | false      | Spans 100% width of the container when enabled.                                                                                                                                                                                                                                                                                                                                    |
| variant              | InputSignal<"outlined" \| "filled">        | 'outlined' | Specifies the input variant of the component.                                                                                                                                                                                                                                                                                                                                      |
| size                 | InputSignal<"small" \| "large">            | undefined  | Specifies the size of the component.                                                                                                                                                                                                                                                                                                                                               |
| inputSize            | InputSignal<number>                        | undefined  | Specifies the visible width of the input element in characters.                                                                                                                                                                                                                                                                                                                    |
| pattern              | InputSignal<string>                        | undefined  | Specifies the value must match the pattern.                                                                                                                                                                                                                                                                                                                                        |
| min                  | InputSignal<number>                        | undefined  | The value must be greater than or equal to the value.                                                                                                                                                                                                                                                                                                                              |
| max                  | InputSignal<number>                        | undefined  | The value must be less than or equal to the value.                                                                                                                                                                                                                                                                                                                                 |
| step                 | InputSignal<number>                        | undefined  | Unless the step is set to the any literal, the value must be min + an integral multiple of the step.                                                                                                                                                                                                                                                                               |
| minlength            | InputSignal<number>                        | undefined  | The number of characters (code points) must not be less than the value of the attribute, if non-empty.                                                                                                                                                                                                                                                                             |
| maxlength            | InputSignal<number>                        | undefined  | The number of characters (code points) must not exceed the value of the attribute.                                                                                                                                                                                                                                                                                                 |
| showButtons          | boolean                                    | false      | Displays spinner buttons.                                                                                                                                                                                                                                                                                                                                                          |
| format               | boolean                                    | true       | Whether to format the value.                                                                                                                                                                                                                                                                                                                                                       |
| buttonLayout         | string                                     | stacked    | Layout of the buttons, valid values are "stacked" (default), "horizontal" and "vertical".                                                                                                                                                                                                                                                                                          |
| inputId              | string                                     | -          | Identifier of the focus input to match a label defined for the component.                                                                                                                                                                                                                                                                                                          |
| placeholder          | string                                     | -          | Advisory information to display on input.                                                                                                                                                                                                                                                                                                                                          |
| tabindex             | number                                     | -          | Specifies tab order of the element.                                                                                                                                                                                                                                                                                                                                                |
| title                | string                                     | -          | Title text of the input text.                                                                                                                                                                                                                                                                                                                                                      |
| ariaLabelledBy       | string                                     | -          | Specifies one or more IDs in the DOM that labels the input field.                                                                                                                                                                                                                                                                                                                  |
| ariaDescribedBy      | string                                     | -          | Specifies one or more IDs in the DOM that describes the input field.                                                                                                                                                                                                                                                                                                               |
| ariaLabel            | string                                     | -          | Used to define a string that labels the input element.                                                                                                                                                                                                                                                                                                                             |
| ariaRequired         | boolean                                    | false      | Used to indicate that user input is required on an element before a form can be submitted.                                                                                                                                                                                                                                                                                         |
| autocomplete         | string                                     | -          | Used to define a string that autocomplete attribute the current element.                                                                                                                                                                                                                                                                                                           |
| incrementButtonClass | string                                     | -          | Style class of the increment button.                                                                                                                                                                                                                                                                                                                                               |
| decrementButtonClass | string                                     | -          | Style class of the decrement button.                                                                                                                                                                                                                                                                                                                                               |
| incrementButtonIcon  | string                                     | -          | Style class of the increment button.                                                                                                                                                                                                                                                                                                                                               |
| decrementButtonIcon  | string                                     | -          | Style class of the decrement button.                                                                                                                                                                                                                                                                                                                                               |
| readonly             | boolean                                    | false      | When present, it specifies that an input field is read-only.                                                                                                                                                                                                                                                                                                                       |
| allowEmpty           | boolean                                    | true       | Determines whether the input field is empty.                                                                                                                                                                                                                                                                                                                                       |
| locale               | string                                     | -          | Locale to be used in formatting.                                                                                                                                                                                                                                                                                                                                                   |
| localeMatcher        | any                                        | -          | The locale matching algorithm to use. Possible values are "lookup" and "best fit"; the default is "best fit". See Locale Negotiation for details.                                                                                                                                                                                                                                  |
| mode                 | any                                        | decimal    | Defines the behavior of the component, valid values are "decimal" and "currency".                                                                                                                                                                                                                                                                                                  |
| currency             | string                                     | -          | The currency to use in currency formatting. Possible values are the ISO 4217 currency codes, such as "USD" for the US dollar, "EUR" for the euro, or "CNY" for the Chinese RMB. There is no default value; if the style is "currency", the currency property must be provided.                                                                                                     |
| currencyDisplay      | any                                        | -          | How to display the currency in currency formatting. Possible values are "symbol" to use a localized currency symbol such as €, ü"code" to use the ISO currency code, "name" to use a localized currency name such as "dollar"; the default is "symbol".                                                                                                                            |
| useGrouping          | boolean                                    | true       | Whether to use grouping separators, such as thousands separators or thousand/lakh/crore separators.                                                                                                                                                                                                                                                                                |
| minFractionDigits    | number                                     | -          | The minimum number of fraction digits to use. Possible values are from 0 to 20; the default for plain number and percent formatting is 0; the default for currency formatting is the number of minor unit digits provided by the ISO 4217 currency code list (2 if the list doesn't provide that information).                                                                     |
| maxFractionDigits    | number                                     | -          | The maximum number of fraction digits to use. Possible values are from 0 to 20; the default for plain number formatting is the larger of minimumFractionDigits and 3; the default for currency formatting is the larger of minimumFractionDigits and the number of minor unit digits provided by the ISO 4217 currency code list (2 if the list doesn't provide that information). |
| prefix               | string                                     | -          | Text to display before the value.                                                                                                                                                                                                                                                                                                                                                  |
| suffix               | string                                     | -          | Text to display after the value.                                                                                                                                                                                                                                                                                                                                                   |
| inputStyle           | any                                        | -          | Inline style of the input field.                                                                                                                                                                                                                                                                                                                                                   |
| inputStyleClass      | string                                     | -          | Style class of the input field.                                                                                                                                                                                                                                                                                                                                                    |
| showClear            | boolean                                    | false      | When enabled, a clear icon is displayed to clear the value.                                                                                                                                                                                                                                                                                                                        |
| autofocus            | boolean                                    | false      | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                                                                                                                                              |

## Outputs

| Name      | Parameters                   | Description                                           |
| --------- | ---------------------------- | ----------------------------------------------------- |
| onInput   | event: InputNumberInputEvent | Callback to invoke on input.                          |
| onFocus   | event: Event                 | Callback to invoke when the component receives focus. |
| onBlur    | event: Event                 | Callback to invoke when the component loses focus.    |
| onKeyDown | event: KeyboardEvent         | Callback to invoke on input key press.                |
| onClear   | value: void                  | Callback to invoke when clear token is clicked.       |

## Templates

| Name                | Type              | Description                            |
| ------------------- | ----------------- | -------------------------------------- |
| clearicon           | TemplateRef<void> | Custom clear icon template.            |
| incrementbuttonicon | TemplateRef<void> | Custom increment button icon template. |
| decrementbuttonicon | TemplateRef<void> | Custom decrement button icon template. |

**Full API & more examples:** https://primeng.org/inputnumber
