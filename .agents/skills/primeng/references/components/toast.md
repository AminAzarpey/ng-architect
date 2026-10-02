# Toast (`p-toast`)

Toast is used to display messages in an overlay.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { ToastModule } from "primeng/toast";
import { MessageService } from "primeng/api";
```

## Example

```typescript
import { Component, inject } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { ToastModule } from "primeng/toast";
import { MessageService } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-toast />
      <p-button (onClick)="show()" label="Show" />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, ToastModule],
  providers: [MessageService],
})
export class ToastBasicDemo {
  private messageService = inject(MessageService);
}
```

## Inputs

| Name                  | Type                       | Default | Description                                                                                 |
| --------------------- | -------------------------- | ------- | ------------------------------------------------------------------------------------------- |
| key                   | string                     | -       | Key of the message in case message is targeted to a specific toast component.               |
| autoZIndex            | boolean                    | true    | Whether to automatically manage layering.                                                   |
| baseZIndex            | number                     | 0       | Base zIndex value to use in layering.                                                       |
| life                  | number                     | 3000    | The default time to display messages for in milliseconds.                                   |
| position              | ToastPositionType          | -       | Position of the toast in viewport.                                                          |
| preventOpenDuplicates | boolean                    | false   | It does not add the new message if there is already a toast displayed with the same content |
| preventDuplicates     | boolean                    | false   | Displays only once a message with the same content.                                         |
| motionOptions         | InputSignal<MotionOptions> | ...     | The motion options.                                                                         |
| breakpoints           | { [key: string]: any }     | -       | Object literal to define styles per screen size.                                            |

## Outputs

| Name    | Parameters             | Description                                  |
| ------- | ---------------------- | -------------------------------------------- |
| onClose | event: ToastCloseEvent | Callback to invoke when a message is closed. |

## Templates

| Name     | Type                                      | Description               |
| -------- | ----------------------------------------- | ------------------------- |
| template | TemplateRef<ToastMessageTemplateContext>  | Custom message template.  |
| headless | TemplateRef<ToastHeadlessTemplateContext> | Custom headless template. |

**Full API & more examples:** https://primeng.org/toast
