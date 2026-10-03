# Timeline (`p-timeline`)

Timeline visualizes a series of chained events.

**Import:**

```ts
import { TimelineModule } from "primeng/timeline";
```

## Example

```typescript
import { Component } from "@angular/core";
import { TimelineModule } from "primeng/timeline";

@Component({
  template: `
    <div class="card">
      <p-timeline [value]="events">
        <ng-template #content let-event>
          {{ event.status }}
        </ng-template>
      </p-timeline>
    </div>
  `,
  standalone: true,
  imports: [TimelineModule],
})
export class TimelineBasicDemo {
  events: any[];

  constructor() {
    this.events = [
      {
        status: "Ordered",
        date: "15/10/2020 10:30",
        icon: "pi pi-shopping-cart",
        color: "#9C27B0",
        image: "game-controller.jpg",
      },
      {
        status: "Processing",
        date: "15/10/2020 14:00",
        icon: "pi pi-cog",
        color: "#673AB7",
      },
      {
        status: "Shipped",
        date: "15/10/2020 16:15",
        icon: "pi pi-shopping-cart",
        color: "#FF9800",
      },
      {
        status: "Delivered",
        date: "16/10/2020 10:00",
        icon: "pi pi-check",
        color: "#607D8B",
      },
    ];
  }
}
```

## Inputs

| Name   | Type                       | Default  | Description                                                                                                                                           |
| ------ | -------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| value  | any[]                      | -        | An array of events to display.                                                                                                                        |
| align  | string                     | left     | Position of the timeline bar relative to the content. Valid values are "left", "right" for vertical layout and "top", "bottom" for horizontal layout. |
| layout | "vertical" \| "horizontal" | vertical | Orientation of the timeline.                                                                                                                          |

## Templates

| Name     | Type                                          | Description                    |
| -------- | --------------------------------------------- | ------------------------------ |
| content  | TemplateRef<TimelineItemTemplateContext<any>> | Custom content template.       |
| opposite | TemplateRef<TimelineItemTemplateContext<any>> | Custom opposite item template. |
| marker   | TemplateRef<TimelineItemTemplateContext<any>> | Custom marker template.        |

**Full API & more examples:** https://primeng.org/timeline
