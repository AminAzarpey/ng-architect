# Speed Dial (`p-speeddial`)

SpeedDial is a floating button with a popup menu.

**Import:**

```ts
import { SpeedDialModule } from "primeng/speeddial";
import { ToastModule } from "primeng/toast";
import { MenuItem, MessageService } from "primeng/api";
```

## Example

```typescript
import { Component, OnInit, inject } from "@angular/core";
import { SpeedDialModule } from "primeng/speeddial";
import { ToastModule } from "primeng/toast";
import { MenuItem, MessageService } from "primeng/api";

@Component({
  template: `
    <div class="card">
      <div
        style="position:relative; height: 500px;"
        class="flex items-center justify-center"
      >
        <p-toast />
        <p-speeddial
          [model]="items"
          [radius]="80"
          type="circle"
          [style]="{ position: 'absolute' }"
          [buttonProps]="{ severity: 'warn', rounded: true }"
        />
      </div>
    </div>
  `,
  standalone: true,
  imports: [SpeedDialModule, ToastModule],
  providers: [MessageService],
})
export class SpeeddialCircleDemo implements OnInit {
  private messageService = inject(MessageService);
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      {
        icon: "pi pi-pencil",
        command: () => {
          this.messageService.add({
            severity: "info",
            summary: "Add",
            detail: "Data Added",
          });
        },
      },
      {
        icon: "pi pi-refresh",
        command: () => {
          this.messageService.add({
            severity: "success",
            summary: "Update",
            detail: "Data Updated",
          });
        },
      },
      {
        icon: "pi pi-trash",
        command: () => {
          this.messageService.add({
            severity: "error",
            summary: "Delete",
            detail: "Data Deleted",
          });
        },
      },
      {
        icon: "pi pi-upload",
        routerLink: ["/fileupload"],
      },
      {
        icon: "pi pi-external-link",
        target: "_blank",
        url: "https://angular.dev",
      },
    ];
  }
}
```

## Inputs

| Name               | Type                                                      | Default | Description                                                                                                                                |
| ------------------ | --------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| id                 | string                                                    | -       | List of items id.                                                                                                                          |
| model              | MenuItem[]                                                | null    | MenuModel instance to define the action items.                                                                                             |
| visible            | boolean                                                   | -       | Specifies the visibility of the overlay.                                                                                                   |
| style              | { [klass: string]: any }                                  | -       | Inline style of the element.                                                                                                               |
| className          | string                                                    | -       | Style class of the element.                                                                                                                |
| transitionDelay    | number                                                    | 30      | Transition delay step for each action item.                                                                                                |
| type               | "circle" \| "linear" \| "semi-circle" \| "quarter-circle" | linear  | Specifies the opening type of actions.                                                                                                     |
| radius             | number                                                    | 0       | Radius for \*circle types.                                                                                                                 |
| mask               | boolean                                                   | false   | Whether to show a mask element behind the speeddial.                                                                                       |
| disabled           | boolean                                                   | false   | Whether the component is disabled.                                                                                                         |
| hideOnClickOutside | boolean                                                   | true    | Whether the actions close when clicked outside.                                                                                            |
| buttonStyle        | { [klass: string]: any }                                  | -       | Inline style of the button element.                                                                                                        |
| buttonClassName    | string                                                    | -       | Style class of the button element.                                                                                                         |
| maskStyle          | { [klass: string]: any }                                  | -       | Inline style of the mask element.                                                                                                          |
| maskClassName      | string                                                    | -       | Style class of the mask element.                                                                                                           |
| showIcon           | string                                                    | -       | Show icon of the button element.                                                                                                           |
| hideIcon           | string                                                    | -       | Hide icon of the button element.                                                                                                           |
| rotateAnimation    | boolean                                                   | true    | Defined to rotate showIcon when hideIcon is not present.                                                                                   |
| ariaLabel          | string                                                    | -       | Defines a string value that labels an interactive element.                                                                                 |
| ariaLabelledBy     | string                                                    | -       | Identifier of the underlying input element.                                                                                                |
| tooltipOptions     | TooltipOptions                                            | -       | Whether to display the tooltip on items. The modifiers of Tooltip can be used like an object in it. Valid keys are 'event' and 'position'. |
| buttonProps        | ButtonProps                                               | -       | Used to pass all properties of the ButtonProps to the Button component.                                                                    |

## Outputs

| Name            | Parameters        | Description                                   |
| --------------- | ----------------- | --------------------------------------------- |
| onVisibleChange | value: boolean    | Fired when the visibility of element changed. |
| visibleChange   | value: boolean    | Fired when the visibility of element changed. |
| onClick         | event: MouseEvent | Fired when the button element clicked.        |
| onShow          | event: Event      | Fired when the actions are visible.           |
| onHide          | event: Event      | Fired when the actions are hidden.            |

## Templates

| Name   | Type                                        | Description             |
| ------ | ------------------------------------------- | ----------------------- |
| button | TemplateRef<SpeedDialButtonTemplateContext> | Custom button template. |
| item   | TemplateRef<SpeedDialItemTemplateContext>   | Custom item template.   |
| icon   | TemplateRef<void>                           | Custom icon template.   |

**Full API & more examples:** https://primeng.org/speeddial
