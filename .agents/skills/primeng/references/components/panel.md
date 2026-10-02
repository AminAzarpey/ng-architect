# Panel (`p-panel`)

Panel is a container component with an optional content toggle feature.

**Import:**

```ts
import { PanelModule } from "primeng/panel";
```

## Example

```typescript
import { Component } from "@angular/core";
import { PanelModule } from "primeng/panel";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-panel header="Header">
        <p class="m-0">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </p-panel>
    </div>
  `,
  standalone: true,
  imports: [PanelModule],
})
export class PanelBasicDemo {}
```

## Inputs

| Name              | Type                         | Default | Description                                                                          |
| ----------------- | ---------------------------- | ------- | ------------------------------------------------------------------------------------ |
| toggleable        | boolean                      | false   | Defines if content of panel can be expanded and collapsed.                           |
| \_header          | string                       | -       | Header text of the panel.                                                            |
| collapsed         | boolean                      | -       | Defines the initial state of panel content, supports one or two-way binding as well. |
| iconPos           | "center" \| "start" \| "end" | end     | Position of the icons.                                                               |
| showHeader        | boolean                      | true    | Specifies if header of panel cannot be displayed.                                    |
| toggler           | "icon" \| "header"           | icon    | Specifies the toggler element to toggle the panel content.                           |
| toggleButtonProps | any                          | -       | Used to pass all properties of the ButtonProps to the Button component.              |
| motionOptions     | InputSignal<MotionOptions>   | ...     | The motion options.                                                                  |

## Outputs

| Name            | Parameters                    | Description                             |
| --------------- | ----------------------------- | --------------------------------------- |
| collapsedChange | value: boolean                | Emitted when the collapsed changes.     |
| onBeforeToggle  | event: PanelBeforeToggleEvent | Callback to invoke before panel toggle. |
| onAfterToggle   | event: PanelAfterToggleEvent  | Callback to invoke after panel toggle.  |

## Templates

| Name        | Type                                         | Description                             |
| ----------- | -------------------------------------------- | --------------------------------------- |
| header      | TemplateRef<void>                            | Defines template option for header.     |
| icons       | TemplateRef<void>                            | Defines template option for icons.      |
| content     | TemplateRef<void>                            | Defines template option for content.    |
| footer      | TemplateRef<void>                            | Defines template option for footer.     |
| headericons | TemplateRef<PanelHeaderIconsTemplateContext> | Defines template option for headerIcon. |

**Full API & more examples:** https://primeng.org/panel
