# Tooltip (`pTooltip`)

Tooltip directive provides advisory information for a component. Tooltip is integrated within various PrimeNG components.

**Import:**

```ts
import { InputTextModule } from "primeng/inputtext";
import { TooltipModule } from "primeng/tooltip";
```

## Example

```typescript
import { Component } from "@angular/core";
import { InputTextModule } from "primeng/inputtext";
import { TooltipModule } from "primeng/tooltip";

@Component({
  template: `
    <div class="card flex flex-wrap justify-center gap-2">
      <input
        type="text"
        pInputText
        pTooltip="Enter your username"
        [autoHide]="false"
        placeholder="autoHide: false"
      />
      <input
        type="text"
        pInputText
        pTooltip="Enter your username"
        placeholder="autoHide: true"
      />
    </div>
  `,
  standalone: true,
  imports: [InputTextModule, TooltipModule],
})
export class TooltipAutohideDemo {}
```

## Inputs

| Name              | Type                               | Default   | Description                                                                                                                                                                                                                                          |
| ----------------- | ---------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tooltipPosition   | string                             | -         | Position of the tooltip.                                                                                                                                                                                                                             |
| tooltipEvent      | "hover" \| "focus" \| "both"       | hover     | Event to show the tooltip.                                                                                                                                                                                                                           |
| positionStyle     | string                             | -         | Type of CSS position.                                                                                                                                                                                                                                |
| tooltipStyleClass | string                             | -         | Style class of the tooltip.                                                                                                                                                                                                                          |
| tooltipZIndex     | string                             | -         | Whether the z-index should be managed automatically to always go on top or have a fixed value.                                                                                                                                                       |
| escape            | boolean                            | true      | By default the tooltip contents are rendered as text. Set to false to support html tags in the content.                                                                                                                                              |
| showDelay         | number                             | -         | Delay to show the tooltip in milliseconds.                                                                                                                                                                                                           |
| hideDelay         | number                             | -         | Delay to hide the tooltip in milliseconds.                                                                                                                                                                                                           |
| life              | number                             | -         | Time to wait in milliseconds to hide the tooltip even it is active.                                                                                                                                                                                  |
| positionTop       | number                             | -         | Specifies the additional vertical offset of the tooltip from its default position.                                                                                                                                                                   |
| positionLeft      | number                             | -         | Specifies the additional horizontal offset of the tooltip from its default position.                                                                                                                                                                 |
| autoHide          | boolean                            | true      | Whether to hide tooltip when hovering over tooltip content.                                                                                                                                                                                          |
| fitContent        | boolean                            | true      | Automatically adjusts the element position when there is not enough space on the selected position.                                                                                                                                                  |
| hideOnEscape      | boolean                            | true      | Whether to hide tooltip on escape key press.                                                                                                                                                                                                         |
| showOnEllipsis    | boolean                            | false     | Whether to show the tooltip only when the target text overflows (e.g., ellipsis is active).                                                                                                                                                          |
| content           | string \| TemplateRef<HTMLElement> | -         | Content of the tooltip.                                                                                                                                                                                                                              |
| disabled          | boolean                            | -         | When present, it specifies that the component should be disabled.                                                                                                                                                                                    |
| tooltipOptions    | TooltipOptions                     | -         | Specifies the tooltip configuration options for the component.                                                                                                                                                                                       |
| appendTo          | InputSignal<any>                   | 'self'    | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| pTooltipPT        | InputSignal<TooltipPassThrough>    | undefined | Used to pass attributes to DOM elements inside the Tooltip component.                                                                                                                                                                                |
| pTooltipUnstyled  | InputSignal<boolean>               | undefined | Indicates whether the component should be rendered without styles.                                                                                                                                                                                   |

**Full API & more examples:** https://primeng.org/tooltip
