# Fieldset (`p-fieldset`)

Fieldset is a grouping component with a content toggle feature.

**Import:**

```ts
import { FieldsetModule } from "primeng/fieldset";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FieldsetModule } from "primeng/fieldset";

@Component({
  template: `
    <div class="card">
      <p-fieldset legend="Header">
        <p class="m-0">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </p-fieldset>
    </div>
  `,
  standalone: true,
  imports: [FieldsetModule],
})
export class FieldsetBasicDemo {}
```

## Inputs

| Name          | Type                       | Default | Description                                                                    |
| ------------- | -------------------------- | ------- | ------------------------------------------------------------------------------ |
| legend        | string                     | -       | Header text of the fieldset.                                                   |
| toggleable    | boolean                    | false   | When specified, content can toggled by clicking the legend.                    |
| style         | { [klass: string]: any }   | -       | Inline style of the component.                                                 |
| styleClass    | string                     | -       | Style class of the component.                                                  |
| motionOptions | InputSignal<MotionOptions> | ...     | The motion options.                                                            |
| collapsed     | boolean                    | -       | Defines the initial state of content, supports one or two-way binding as well. |

## Outputs

| Name            | Parameters                       | Description                             |
| --------------- | -------------------------------- | --------------------------------------- |
| collapsedChange | value: boolean                   | Emits when the collapsed state changes. |
| onBeforeToggle  | event: FieldsetBeforeToggleEvent | Callback to invoke before panel toggle. |
| onAfterToggle   | event: FieldsetAfterToggleEvent  | Callback to invoke after panel toggle.  |

## Templates

| Name         | Type              | Description                    |
| ------------ | ----------------- | ------------------------------ |
| header       | TemplateRef<void> | Custom header template.        |
| expandicon   | TemplateRef<void> | Custom expand icon template.   |
| collapseicon | TemplateRef<void> | Custom collapse icon template. |
| content      | TemplateRef<void> | Custom content template.       |

**Full API & more examples:** https://primeng.org/fieldset
