# Editor (`p-editor`)

Editor is rich text editor component based on Quill.

**Import:**

```ts
import { EditorModule } from "primeng/editor";
```

## Example

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { EditorModule } from "primeng/editor";

@Component({
  template: `
    <div class="card">
      <p-editor [(ngModel)]="text" [style]="{ height: '320px' }" />
    </div>
  `,
  standalone: true,
  imports: [EditorModule, FormsModule],
})
export class EditorBasicDemo {
  text: string | undefined;
}
```

## Inputs

| Name               | Type                                       | Default   | Description                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| required           | InputSignalWithTransform<boolean, unknown> | false     | There must be a value (if set).                                                                                                                                                                                                                                                                                                               |
| invalid            | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have invalid state style.                                                                                                                                                                                                                                                                |
| disabled           | InputSignalWithTransform<boolean, unknown> | false     | When present, it specifies that the component should have disabled state style.                                                                                                                                                                                                                                                               |
| name               | InputSignal<string>                        | undefined | When present, it specifies that the name of the input.                                                                                                                                                                                                                                                                                        |
| style              | { [klass: string]: any }                   | -         | Inline style of the container.                                                                                                                                                                                                                                                                                                                |
| placeholder        | string                                     | -         | Placeholder text to show when editor is empty.                                                                                                                                                                                                                                                                                                |
| formats            | string[]                                   | -         | Whitelist of formats to display, see [here](https://quilljs.com/docs/formats/) for available options.                                                                                                                                                                                                                                         |
| modules            | object                                     | -         | Modules configuration of Editor, see [here](https://quilljs.com/docs/modules/) for available options.                                                                                                                                                                                                                                         |
| bounds             | string \| HTMLElement                      | -         | DOM Element or a CSS selector for a DOM Element, within which the editor’s p elements (i.e. tooltips, etc.) should be confined. Currently, it only considers left and right boundaries.                                                                                                                                                       |
| scrollingContainer | string \| HTMLElement                      | -         | DOM Element or a CSS selector for a DOM Element, specifying which container has the scrollbars (i.e. overflow-y: auto), if is has been changed from the default ql-editor with custom CSS. Necessary to fix scroll jumping bugs when Quill is set to auto grow its height, and another ancestor container is responsible from the scrolling.. |
| debug              | string                                     | -         | Shortcut for debug. Note debug is a static method and will affect other instances of Quill editors on the page. Only warning and error messages are enabled by default.                                                                                                                                                                       |
| readonly           | boolean                                    | -         | Whether to instantiate the editor to read-only mode.                                                                                                                                                                                                                                                                                          |

## Outputs

| Name              | Parameters                        | Description                                                                                |
| ----------------- | --------------------------------- | ------------------------------------------------------------------------------------------ |
| onEditorInit      | event: EditorInitEvent            | Callback to invoke when the quill modules are loaded.                                      |
| onTextChange      | event: EditorTextChangeEvent      | Callback to invoke when text of editor changes.                                            |
| onSelectionChange | event: EditorSelectionChangeEvent | Callback to invoke when selection of the text changes.                                     |
| onEditorChange    | event: EditorChangeEvent          | Callback to invoke when editor content changes (combines both text and selection changes). |
| onFocus           | event: EditorFocusEvent           | Callback to invoke when editor receives focus.                                             |
| onBlur            | event: EditorBlurEvent            | Callback to invoke when editor loses focus.                                                |

## Templates

| Name   | Type             | Description           |
| ------ | ---------------- | --------------------- |
| header | TemplateRef<any> | Custom item template. |

**Full API & more examples:** https://primeng.org/editor
