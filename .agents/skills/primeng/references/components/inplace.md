# Inplace (`p-inplace`)

Inplace provides an easy to do editing and display at the same time where clicking the output displays the actual content.

**Import:**

```ts
import { InplaceModule } from "primeng/inplace";
```

## Example

```typescript
import { Component } from "@angular/core";
import { InplaceModule } from "primeng/inplace";

@Component({
  template: `
    <div class="card">
      <p-inplace>
        <ng-template #display>
          <span>View Content</span>
        </ng-template>
        <ng-template #content>
          <p class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </ng-template>
      </p-inplace>
    </div>
  `,
  standalone: true,
  imports: [InplaceModule],
})
export class InplaceBasicDemo {}
```

## Inputs

| Name           | Type    | Default | Description                                                     |
| -------------- | ------- | ------- | --------------------------------------------------------------- |
| active         | boolean | false   | Whether the content is displayed or not.                        |
| disabled       | boolean | false   | When present, it specifies that the element should be disabled. |
| preventClick   | boolean | false   | Allows to prevent clicking.                                     |
| closeAriaLabel | string  | -       | Establishes a string value that labels the close button.        |

## Outputs

| Name         | Parameters   | Description                                |
| ------------ | ------------ | ------------------------------------------ |
| onActivate   | event: Event | Callback to invoke when inplace is opened. |
| onDeactivate | event: Event | Callback to invoke when inplace is closed. |

## Templates

| Name      | Type                                       | Description                 |
| --------- | ------------------------------------------ | --------------------------- |
| display   | TemplateRef<void>                          | Custom display template.    |
| content   | TemplateRef<InplaceContentTemplateContext> | Custom content template.    |
| closeicon | TemplateRef<void>                          | Custom close icon template. |

## Methods

| Name       | Parameters   | Return Type | Description              |
| ---------- | ------------ | ----------- | ------------------------ |
| activate   | event: Event | void        | Activates the content.   |
| deactivate | event: Event | void        | Deactivates the content. |

**Full API & more examples:** https://primeng.org/inplace
