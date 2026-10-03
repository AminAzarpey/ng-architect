# Message (`p-message`)

Message component is used to display inline messages.

**Import:**

```ts
import { MessageModule } from "primeng/message";
```

## Example

```typescript
import { Component } from "@angular/core";
import { MessageModule } from "primeng/message";

@Component({
  template: `
    <div class="card">
      <p-message>Message Content</p-message>
    </div>
  `,
  standalone: true,
  imports: [MessageModule],
})
export class MessageBasicDemo {}
```

## Inputs

| Name          | Type                                                                  | Default   | Description                                                      |
| ------------- | --------------------------------------------------------------------- | --------- | ---------------------------------------------------------------- |
| severity      | "success" \| "info" \| "warn" \| "secondary" \| "contrast" \| "error" | 'info'    | Severity level of the message.                                   |
| style         | { [klass: string]: any }                                              | -         | Inline style of the component.                                   |
| styleClass    | string                                                                | -         | Style class of the component.                                    |
| closable      | boolean                                                               | false     | Whether the message can be closed manually using the close icon. |
| icon          | string                                                                | undefined | Icon to display in the message.                                  |
| closeIcon     | string                                                                | undefined | Icon to display in the message close button.                     |
| size          | "small" \| "large"                                                    | -         | Defines the size of the component.                               |
| variant       | "text" \| "outlined" \| "simple"                                      | -         | Specifies the input variant of the component.                    |
| motionOptions | InputSignal<MotionOptions>                                            | ...       | The motion options.                                              |

## Outputs

| Name    | Parameters                      | Description                       |
| ------- | ------------------------------- | --------------------------------- |
| onClose | event: { originalEvent: Event } | Emits when the message is closed. |

## Templates

| Name      | Type                                         | Description                               |
| --------- | -------------------------------------------- | ----------------------------------------- |
| container | TemplateRef<MessageContainerTemplateContext> | Custom template of the message container. |
| icon      | TemplateRef<void>                            | Custom template of the message icon.      |
| closeicon | TemplateRef<void>                            | Custom template of the close icon.        |

## Methods

| Name  | Parameters   | Return Type | Description         |
| ----- | ------------ | ----------- | ------------------- |
| close | event: Event | void        | Closes the message. |

**Full API & more examples:** https://primeng.org/message
