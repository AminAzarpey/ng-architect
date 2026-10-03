# SplitButton (`p-splitbutton`)

SplitButton groups a set of commands in an overlay with a default action item.

**Import:**

```ts
import { SplitButtonModule } from "primeng/splitbutton";
import { ToastModule } from "primeng/toast";
import { MenuItem, MessageService } from "primeng/api";
```

## Example

```typescript
import { Component, inject } from "@angular/core";
import { SplitButtonModule } from "primeng/splitbutton";
import { ToastModule } from "primeng/toast";
import { MenuItem, MessageService } from "primeng/api";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-toast />
      <p-splitbutton label="Save" (onClick)="save()" [model]="items" />
    </div>
  `,
  standalone: true,
  imports: [SplitButtonModule, ToastModule],
  providers: [MessageService],
})
export class SplitbuttonBasicDemo {
  private messageService = inject(MessageService);

  constructor() {
    this.items = [
      {
        label: "Update",
        command: () => {
          this.update();
        },
      },
      {
        label: "Delete",
        command: () => {
          this.delete();
        },
      },
      { label: "Angular.dev", url: "https://angular.dev" },
      { separator: true },
      { label: "Upload", routerLink: ["/fileupload"] },
    ];
  }

  save() {
    this.messageService.add({
      severity: "success",
      summary: "Success",
      detail: "Data Saved",
    });
  }

  update() {
    this.messageService.add({
      severity: "success",
      summary: "Updated",
      detail: "Data Updated",
    });
  }

  delete() {
    this.messageService.add({
      severity: "warn",
      summary: "Delete",
      detail: "Data Deleted",
    });
  }
}
```

## Inputs

| Name               | Type                                                                                          | Default | Description                                                                                                                                                                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model              | MenuItem[]                                                                                    | -       | MenuModel instance to define the overlay items.                                                                                                                                                                                                      |
| severity           | "success" \| "info" \| "warn" \| "danger" \| "help" \| "primary" \| "secondary" \| "contrast" | -       | Defines the style of the button.                                                                                                                                                                                                                     |
| raised             | boolean                                                                                       | false   | Add a shadow to indicate elevation.                                                                                                                                                                                                                  |
| rounded            | boolean                                                                                       | false   | Add a circular border radius to the button.                                                                                                                                                                                                          |
| text               | boolean                                                                                       | false   | Add a textual class to the button without a background initially.                                                                                                                                                                                    |
| outlined           | boolean                                                                                       | false   | Add a border class without a background initially.                                                                                                                                                                                                   |
| size               | "small" \| "large"                                                                            | null    | Defines the size of the button.                                                                                                                                                                                                                      |
| plain              | boolean                                                                                       | false   | Add a plain textual class to the button without a background initially.                                                                                                                                                                              |
| icon               | string                                                                                        | -       | Name of the icon.                                                                                                                                                                                                                                    |
| iconPos            | SplitButtonIconPosition                                                                       | left    | Position of the icon.                                                                                                                                                                                                                                |
| label              | string                                                                                        | -       | Text of the button.                                                                                                                                                                                                                                  |
| tooltip            | string                                                                                        | -       | Tooltip for the main button.                                                                                                                                                                                                                         |
| tooltipOptions     | TooltipOptions                                                                                | -       | Tooltip options for the main button.                                                                                                                                                                                                                 |
| menuStyle          | { [klass: string]: any }                                                                      | -       | Inline style of the overlay menu.                                                                                                                                                                                                                    |
| menuStyleClass     | string                                                                                        | -       | Style class of the overlay menu.                                                                                                                                                                                                                     |
| dropdownIcon       | string                                                                                        | -       | Name of the dropdown icon.                                                                                                                                                                                                                           |
| appendTo           | InputSignal<any>                                                                              | 'body'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| dir                | string                                                                                        | -       | Indicates the direction of the element.                                                                                                                                                                                                              |
| expandAriaLabel    | string                                                                                        | -       | Defines a string that labels the expand button for accessibility.                                                                                                                                                                                    |
| motionOptions      | InputSignal<MotionOptions>                                                                    | ...     | The motion options.                                                                                                                                                                                                                                  |
| autofocus          | boolean                                                                                       | false   | When present, it specifies that the component should automatically get focus on load.                                                                                                                                                                |
| disabled           | boolean                                                                                       | -       | When present, it specifies that the element should be disabled.                                                                                                                                                                                      |
| tabindex           | number                                                                                        | -       | Index of the element in tabbing order.                                                                                                                                                                                                               |
| menuButtonDisabled | boolean                                                                                       | false   | When present, it specifies that the menu button element should be disabled.                                                                                                                                                                          |
| buttonDisabled     | boolean                                                                                       | false   | When present, it specifies that the button element should be disabled.                                                                                                                                                                               |

## Outputs

| Name            | Parameters        | Description                                                |
| --------------- | ----------------- | ---------------------------------------------------------- |
| onClick         | event: MouseEvent | Callback to invoke when default command button is clicked. |
| onMenuHide      | value: any        | Callback to invoke when overlay menu is hidden.            |
| onMenuShow      | value: any        | Callback to invoke when overlay menu is shown.             |
| onDropdownClick | event: MouseEvent | Callback to invoke when dropdown button is clicked.        |

## Templates

| Name         | Type              | Description                    |
| ------------ | ----------------- | ------------------------------ |
| content      | TemplateRef<void> | Custom content template.       |
| dropdownicon | TemplateRef<void> | Custom dropdown icon template. |

**Full API & more examples:** https://primeng.org/splitbutton
