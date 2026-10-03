# Scroll Top (`p-scrolltop`)

ScrollTop gets displayed after a certain scroll position and used to navigates to the top of the page quickly.

**Import:**

```ts
import { ScrollTopModule } from "primeng/scrolltop";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ScrollTopModule } from "primeng/scrolltop";

@Component({
  template: `
    <div class="card flex flex-col items-center">
      <p>Scroll down the page to display the ScrollTo component.</p>
      <i
        class="pi pi-angle-down animate-fadeout animate-duration-1000 animate-infinite"
        style="fontsize: 2rem; margin-bottom: 30rem"
      ></i>
      <p-scrolltop />
    </div>
  `,
  standalone: true,
  imports: [ScrollTopModule],
})
export class ScrolltopBasicDemo {}
```

## Inputs

| Name            | Type                       | Default | Description                                                                                         |
| --------------- | -------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| styleClass      | string                     | -       | Class of the element.                                                                               |
| style           | { [klass: string]: any }   | -       | Inline style of the element.                                                                        |
| target          | "window" \| "parent"       | window  | Target of the ScrollTop.                                                                            |
| threshold       | number                     | 400     | Defines the threshold value of the vertical scroll position of the target to toggle the visibility. |
| icon            | string                     | -       | Name of the icon or JSX.Element for icon.                                                           |
| behavior        | "auto" \| "smooth"         | smooth  | Defines the scrolling behavior, "smooth" adds an animation and "auto" scrolls with a jump.          |
| motionOptions   | InputSignal<MotionOptions> | ...     | The motion options.                                                                                 |
| buttonAriaLabel | string                     | -       | Establishes a string value that labels the scroll-top button.                                       |
| buttonProps     | ButtonProps                | ...     | Used to pass all properties of the ButtonProps to the Button component.                             |

## Templates

| Name | Type                                      | Description           |
| ---- | ----------------------------------------- | --------------------- |
| icon | TemplateRef<ScrollTopIconTemplateContext> | Custom icon template. |

**Full API & more examples:** https://primeng.org/scrolltop
