# Overlay API - PrimeNG (`p-overlay`)

This API allows overlay components to be controlled from the PrimeNG. In this way, all overlay components in the application can have the same behavior.

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
      <p-button (click)="toggle()" label="Show Overlay"></p-button>
      <p-overlay
        [(visible)]="overlayVisible"
        [responsive]="{
          breakpoint: '640px',
          direction: 'bottom',
          contentStyleClass: 'h-20rem',
        }"
        contentStyleClass="p-6 bg-surface-0 dark:bg-surface-900 shadow rounded-border"
      >
        Content
      </p-overlay>
    </div>
  `,
  standalone: true,
  imports: [ButtonModule],
})
export class OverlayBasicDemo {
  overlayVisible: boolean = false;

  toggle() {
    this.overlayVisible = !this.overlayVisible;
  }
}
```

## Inputs

| Name              | Type                       | Default | Description                                                                                                                                                                                                                                          |
| ----------------- | -------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| visible           | boolean                    | -       | The visible property is an input that determines the visibility of the component.                                                                                                                                                                    |
| mode              | string                     | -       | The mode property is an input that determines the overlay mode type or string.                                                                                                                                                                       |
| style             | { [klass: string]: any }   | -       | The style property is an input that determines the style object for the component.                                                                                                                                                                   |
| styleClass        | string                     | -       | The styleClass property is an input that determines the CSS class(es) for the component.                                                                                                                                                             |
| contentStyle      | { [klass: string]: any }   | -       | The contentStyle property is an input that determines the style object for the content of the component.                                                                                                                                             |
| contentStyleClass | string                     | -       | The contentStyleClass property is an input that determines the CSS class(es) for the content of the component.                                                                                                                                       |
| target            | string                     | -       | The target property is an input that specifies the target element or selector for the component.                                                                                                                                                     |
| autoZIndex        | boolean                    | -       | The autoZIndex determines whether to automatically manage layering. Its default value is 'false'.                                                                                                                                                    |
| baseZIndex        | number                     | -       | The baseZIndex is base zIndex value to use in layering.                                                                                                                                                                                              |
| listener          | any                        | -       | The listener property is an input that specifies the listener object for the component.                                                                                                                                                              |
| responsive        | ResponsiveOverlayOptions   | -       | It is the option used to determine in which mode it should appear according to the given media or breakpoint.                                                                                                                                        |
| options           | OverlayOptions             | -       | The options property is an input that specifies the overlay options for the component.                                                                                                                                                               |
| appendTo          | InputSignal<any>           | 'self'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| inline            | InputSignal<boolean>       | false   | Specifies whether the overlay should be rendered inline within the current component's template.                                                                                                                                                     |
| motionOptions     | InputSignal<MotionOptions> | ...     | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name             | Parameters                      | Description                                                                         |
| ---------------- | ------------------------------- | ----------------------------------------------------------------------------------- |
| visibleChange    | value: boolean                  | This EventEmitter is used to notify changes in the visibility state of a component. |
| onBeforeShow     | event: OverlayOnBeforeShowEvent | Callback to invoke before the overlay is shown.                                     |
| onShow           | event: OverlayOnShowEvent       | Callback to invoke when the overlay is shown.                                       |
| onBeforeHide     | event: OverlayOnBeforeHideEvent | Callback to invoke before the overlay is hidden.                                    |
| onHide           | event: OverlayOnHideEvent       | Callback to invoke when the overlay is hidden                                       |
| onAnimationStart | event: AnimationEvent           | Callback to invoke when the animation is started.                                   |
| onAnimationDone  | event: AnimationEvent           | Callback to invoke when the animation is done.                                      |
| onBeforeEnter    | event: MotionEvent              | Callback to invoke before the overlay enters.                                       |
| onEnter          | event: MotionEvent              | Callback to invoke when the overlay enters.                                         |
| onAfterEnter     | event: MotionEvent              | Callback to invoke after the overlay has entered.                                   |
| onBeforeLeave    | event: MotionEvent              | Callback to invoke before the overlay leaves.                                       |
| onLeave          | event: MotionEvent              | Callback to invoke when the overlay leaves.                                         |
| onAfterLeave     | event: MotionEvent              | Callback to invoke after the overlay has left.                                      |

## Templates

| Name    | Type                                       | Description                        |
| ------- | ------------------------------------------ | ---------------------------------- |
| content | TemplateRef<OverlayContentTemplateContext> | Content template of the component. |

**Full API & more examples:** https://primeng.org/overlay
