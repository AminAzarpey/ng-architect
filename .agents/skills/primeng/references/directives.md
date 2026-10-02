# Utility Directives

PrimeNG ships standalone attribute directives for behaviors that aren't full components. Import the directive (or its module) into the host component's `imports`. Each has a full reference under `components/`.

| Directive       | Selector                    | Purpose                                                                                                        | Reference                                        |
| --------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Ripple          | `pRipple`                   | Material-style ripple on click. Enable globally with `providePrimeNG({ ripple: true })`.                       | [ripple](components/ripple.md)                   |
| StyleClass      | `pStyleClass`               | Declaratively toggle/animate CSS classes on a target during enter/leave.                                       | [styleclass](components/styleclass.md)           |
| Tooltip         | `pTooltip`                  | Advisory text on hover/focus; `tooltipPosition`, etc.                                                          | [tooltip](components/tooltip.md)                 |
| FocusTrap       | `pFocusTrap`                | Keep keyboard focus within a DOM element while tabbing.                                                        | [focustrap](components/focustrap.md)             |
| AutoFocus       | `pAutoFocus`                | Focus a focusable element on load (`[pAutoFocus]="true"`).                                                     | [autofocus](components/autofocus.md)             |
| KeyFilter       | `pKeyFilter`                | Restrict keystrokes to a pattern (e.g. `"int"`, `"money"`). For whole-input formats use InputNumber/InputMask. | [keyfilter](components/keyfilter.md)             |
| AnimateOnScroll | `pAnimateOnScroll`          | Apply enter/leave animations as elements enter/leave the viewport.                                             | [animateonscroll](components/animateonscroll.md) |
| DragDrop        | `pDraggable` / `pDroppable` | Drag-and-drop behavior on any element.                                                                         | [dragdrop](components/dragdrop.md)               |

Example:

```ts
import { RippleModule } from "primeng/ripple";
import { TooltipModule } from "primeng/tooltip";

@Component({
  standalone: true,
  imports: [RippleModule, TooltipModule],
  template: `<div pRipple pTooltip="Hello" tooltipPosition="top" class="card">
    Click
  </div>`,
})
export class DemoComponent {}
```

`InputText` (`pInputText`) and `Textarea` (`pTextarea`) are also directives applied to native `<input>`/`<textarea>` — see [components/inputtext.md](components/inputtext.md) and [components/textarea.md](components/textarea.md).
