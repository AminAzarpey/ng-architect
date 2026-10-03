# Button (`p-button`)

Button is an extension to standard button element with icons and theming.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ButtonModule } from "primeng/button";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-button label="Submit" />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule],
})
export class ButtonBasicDemo {}
```

## Directive usage (`pButton`)

Besides the `<p-button>` component, PrimeNG ships a **`pButton` directive** that applies
button styling to a native `<button>` **or `<a>` element**. Use it when you need a real
anchor — most commonly with `routerLink` — or any native element semantics. Label and icon
are projected with the `pButtonLabel` and `pButtonIcon` helper directives (not the `label`/
`icon` inputs).

```html
<!-- native button -->
<button pButton>
  <i class="pi pi-check" pButtonIcon></i>
  <span pButtonLabel>Save</span>
</button>

<!-- anchor styled as a button -->
<a href="https://angular.dev" pButton target="_blank" rel="noopener noreferrer">
  <span pButtonLabel>External</span>
</a>

<!-- router link styled as a button (very common) -->
<a routerLink="/dashboard" pButton>
  <span pButtonLabel>Dashboard</span>
</a>
```

All the styling inputs below (e.g. `severity`, `outlined`, `rounded`, `size`) work as
attributes on the directive too, e.g. `<a routerLink="/" pButton severity="secondary" outlined>`.

**Gotchas:**

- On a native element use the **native DOM events** — `(click)`, `(focus)`, `(blur)` — **not**
  the component's `(onClick)`/`(onFocus)`/`(onBlur)` outputs (those are for `<p-button>`).
- For `routerLink`, import Angular's `RouterLink` into the component's `imports` alongside
  `ButtonModule`.
- Prefer `<p-button>` for the simple `label`/`icon` case; prefer the `pButton` directive for
  anchors/`routerLink` and when you need a genuine native element.

## Inputs

| Name          | Type                                                                                          | Default   | Description                                                                           |
| ------------- | --------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------- |
| type          | string                                                                                        | button    | Type of the button.                                                                   |
| badge         | string                                                                                        | -         | Value of the badge.                                                                   |
| disabled      | boolean                                                                                       | false     | When present, it specifies that the component should be disabled.                     |
| raised        | boolean                                                                                       | false     | Add a shadow to indicate elevation.                                                   |
| rounded       | boolean                                                                                       | false     | Add a circular border radius to the button.                                           |
| text          | boolean                                                                                       | false     | Add a textual class to the button without a background initially.                     |
| plain         | boolean                                                                                       | false     | Add a plain textual class to the button without a background initially.               |
| outlined      | boolean                                                                                       | false     | Add a border class without a background initially.                                    |
| link          | boolean                                                                                       | false     | Add a link style to the button.                                                       |
| tabindex      | number                                                                                        | -         | Add a tabindex to the button.                                                         |
| size          | "small" \| "large"                                                                            | -         | Defines the size of the button.                                                       |
| variant       | "text" \| "outlined"                                                                          | -         | Specifies the variant of the component.                                               |
| style         | { [klass: string]: any }                                                                      | -         | Inline style of the element.                                                          |
| styleClass    | string                                                                                        | -         | Class of the element.                                                                 |
| badgeSeverity | "success" \| "info" \| "warn" \| "danger" \| "help" \| "primary" \| "secondary" \| "contrast" | secondary | Severity type of the badge.                                                           |
| ariaLabel     | string                                                                                        | -         | Used to define a string that autocomplete attribute the current element.              |
| autofocus     | boolean                                                                                       | false     | When present, it specifies that the component should automatically get focus on load. |
| iconPos       | ButtonIconPosition                                                                            | left      | Position of the icon.                                                                 |
| icon          | string                                                                                        | -         | Name of the icon.                                                                     |
| label         | string                                                                                        | -         | Text of the button.                                                                   |
| loading       | boolean                                                                                       | false     | Whether the button is in loading state.                                               |
| loadingIcon   | string                                                                                        | -         | Icon to display in loading state.                                                     |
| severity      | ButtonSeverity                                                                                | -         | Defines the style of the button.                                                      |
| buttonProps   | ButtonProps                                                                                   | -         | Used to pass all properties of the ButtonProps to the Button component.               |
| fluid         | InputSignalWithTransform<boolean, unknown>                                                    | undefined | Spans 100% width of the container when enabled.                                       |

## Outputs

| Name    | Parameters        | Description                                                                                                                                                 |
| ------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| onClick | event: MouseEvent | Callback to execute when button is clicked. This event is intended to be used with the <p-button> component. Using a regular <button> element, use (click). |
| onFocus | event: FocusEvent | Callback to execute when button is focused. This event is intended to be used with the <p-button> component. Using a regular <button> element, use (focus). |
| onBlur  | event: FocusEvent | Callback to execute when button loses focus. This event is intended to be used with the <p-button> component. Using a regular <button> element, use (blur). |

## Templates

| Name        | Type                                          | Description                   |
| ----------- | --------------------------------------------- | ----------------------------- |
| content     | TemplateRef<void>                             | Custom content template.      |
| loadingicon | TemplateRef<ButtonLoadingIconTemplateContext> | Custom loading icon template. |
| icon        | TemplateRef<ButtonIconTemplateContext>        | Custom icon template.         |

**Full API & more examples:** https://primeng.org/button
