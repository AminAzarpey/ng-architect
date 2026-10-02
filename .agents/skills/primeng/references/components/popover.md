# Popover (`p-popover`)

Popover is a container component that can overlay other components on page.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { InputGroupModule } from "primeng/inputgroup";
import { PopoverModule } from "primeng/popover";
import { InputTextModule } from "primeng/inputtext";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { InputGroupModule } from "primeng/inputgroup";
import { PopoverModule } from "primeng/popover";
import { InputTextModule } from "primeng/inputtext";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-button
        (click)="op.toggle($event)"
        icon="pi pi-share-alt"
        label="Share"
      />
      <p-popover #op>
        <div class="flex flex-col gap-4 w-[25rem]">
          <div>
            <span
              class="font-medium text-surface-900 dark:text-surface-0 block mb-2"
              >Share this document</span
            >
            <p-inputgroup>
              <input
                pInputText
                value="https://primeng.org/12323ff26t2g243g423g234gg52hy25XADXAG3"
                readonly
                class="w-[25rem]"
              />
              <p-inputgroup-addon>
                <i class="pi pi-copy"></i>
              </p-inputgroup-addon>
            </p-inputgroup>
          </div>
          <div>
            <span
              class="font-medium text-surface-900 dark:text-surface-0 block mb-2"
              >Invite Member</span
            >
            <div class="flex">
              <p-inputgroup>
                <input pInputText disabled />
                <button pButton label="Invite" icon="pi pi-users"></button>
              </p-inputgroup>
            </div>
          </div>
          <div>
            <span
              class="font-medium text-surface-900 dark:text-surface-0 block mb-2"
              >Team Members</span
            >
            <ul class="list-none p-0 m-0 flex flex-col gap-4">
              @for (member of members; track member) {
                <li class="flex items-center gap-2">
                  <img
                    [src]="
                      'https://primefaces.org/cdn/primeng/images/demo/avatar/' +
                      member.image
                    "
                    style="width: 32px"
                  />
                  <div>
                    <span class="font-medium">{{ member.name }}</span>
                    <div class="text-sm text-muted-color">
                      {{ member.email }}
                    </div>
                  </div>
                  <div
                    class="flex items-center gap-2 text-muted-color ml-auto text-sm"
                  >
                    <span>{{ member.role }}</span>
                    <i class="pi pi-angle-down"></i>
                  </div>
                </li>
              }
            </ul>
          </div>
        </div>
      </p-popover>
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, InputGroupModule, PopoverModule, InputTextModule],
})
export class PopoverBasicDemo {
  members: any[];
}
```

## Inputs

| Name           | Type                       | Default | Description                                                                                                                                                                                                                                          |
| -------------- | -------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ariaLabel      | string                     | -       | Defines a string that labels the input for accessibility.                                                                                                                                                                                            |
| ariaLabelledBy | string                     | -       | Establishes relationships between the component and label(s) where its value should be one or more element IDs.                                                                                                                                      |
| dismissable    | boolean                    | true    | Enables to hide the overlay when outside is clicked.                                                                                                                                                                                                 |
| style          | { [klass: string]: any }   | -       | Inline style of the component.                                                                                                                                                                                                                       |
| styleClass     | string                     | -       | Style class of the component.                                                                                                                                                                                                                        |
| appendTo       | InputSignal<any>           | 'self'  | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| autoZIndex     | boolean                    | true    | Whether to automatically manage layering.                                                                                                                                                                                                            |
| ariaCloseLabel | string                     | -       | Aria label of the close icon.                                                                                                                                                                                                                        |
| baseZIndex     | number                     | 0       | Base zIndex value to use in layering.                                                                                                                                                                                                                |
| focusOnShow    | boolean                    | true    | When enabled, first button receives focus on show.                                                                                                                                                                                                   |
| motionOptions  | InputSignal<MotionOptions> | ...     | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name   | Parameters | Description                                         |
| ------ | ---------- | --------------------------------------------------- |
| onShow | value: any | Callback to invoke when an overlay becomes visible. |
| onHide | value: any | Callback to invoke when an overlay gets hidden.     |

## Templates

| Name    | Type                                       | Description              |
| ------- | ------------------------------------------ | ------------------------ |
| content | TemplateRef<PopoverContentTemplateContext> | Custom content template. |

## Methods

| Name   | Parameters              | Return Type | Description                          |
| ------ | ----------------------- | ----------- | ------------------------------------ |
| toggle | event: any, target: any | void        | Toggles the visibility of the panel. |
| show   | event: any, target: any | void        | Displays the panel.                  |
| hide   |                         | void        | Hides the panel.                     |

**Full API & more examples:** https://primeng.org/popover
