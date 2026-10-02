# Splitter (`p-splitter`)

Splitter is utilized to separate and resize panels.

**Import:**

```ts
import { SplitterModule } from "primeng/splitter";
```

## Example

```typescript
import { Component } from "@angular/core";
import { SplitterModule } from "primeng/splitter";

@Component({
  template: `
    <div class="card">
      <p-splitter [style]="{ height: '300px' }" class="mb-8">
        <ng-template #panel>
          <div class="flex items-center justify-center h-full">Panel 1</div>
        </ng-template>
        <ng-template #panel>
          <div class="flex items-center justify-center h-full">Panel 2</div>
        </ng-template>
      </p-splitter>
    </div>
  `,
  standalone: true,
  imports: [SplitterModule],
})
export class SplitterHorizontalDemo {}
```

## Inputs

| Name            | Type                     | Default    | Description                                                                                                                    |
| --------------- | ------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
| panelStyleClass | string                   | -          | Style class of the panel.                                                                                                      |
| panelStyle      | { [klass: string]: any } | -          | Inline style of the panel.                                                                                                     |
| stateStorage    | string                   | session    | Defines where a stateful splitter keeps its state, valid values are 'session' for sessionStorage and 'local' for localStorage. |
| stateKey        | string                   | null       | Storage identifier of a stateful Splitter.                                                                                     |
| layout          | string                   | horizontal | Orientation of the panels. Valid values are 'horizontal' and 'vertical'.                                                       |
| gutterSize      | number                   | 4          | Size of the divider in pixels.                                                                                                 |
| step            | number                   | 5          | Step factor to increment/decrement the size of the panels while pressing the arrow keys.                                       |
| minSizes        | number[]                 | []         | Minimum size of the elements relative to 100%.                                                                                 |
| panelSizes      | number[]                 | -          | Size of the elements relative to 100%.                                                                                         |

## Outputs

| Name          | Parameters                      | Description                            |
| ------------- | ------------------------------- | -------------------------------------- |
| onResizeEnd   | event: SplitterResizeEndEvent   | Callback to invoke when resize ends.   |
| onResizeStart | event: SplitterResizeStartEvent | Callback to invoke when resize starts. |

**Full API & more examples:** https://primeng.org/splitter
