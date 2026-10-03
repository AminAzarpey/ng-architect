# MegaMenu (`p-megamenu`)

MegaMenu is navigation component that displays submenus together.

**Import:**

```ts
import { MegaMenuModule } from "primeng/megamenu";
import { MegaMenuItem } from "primeng/api";
import { Table } from "primeng/table";
```

## Example

```typescript
import { Component, OnInit } from "@angular/core";
import { MegaMenuModule } from "primeng/megamenu";
import { MegaMenuItem } from "primeng/api";
import { Table } from "primeng/table";

@Component({
  template: `
    <div class="card">
      <p-megamenu [model]="items" />
    </div>
  `,
  standalone: true,
  imports: [MegaMenuModule],
})
export class MegamenuBasicDemo implements OnInit {
  items: MegaMenuItem[] | undefined;

  ngOnInit() {
    this.items = [
      {
        label: "Furniture",
        icon: "pi pi-box",
        items: [
          [
            {
              label: "Living Room",
              items: [
                { label: "Accessories" },
                { label: "Armchair" },
                { label: "Coffee Table" },
                { label: "Couch" },
                { label: "TV Stand" },
              ],
            },
          ],
          [
            {
              label: "Kitchen",
              items: [
                { label: "Bar stool" },
                { label: "Chair" },
                { label: "Table" },
              ],
            },
            {
              label: "Bathroom",
              items: [{ label: "Accessories" }],
            },
          ],
          [
            {
              label: "Bedroom",
              items: [
                { label: "Bed" },
                { label: "Chaise lounge" },
                { label: "Cupboard" },
                { label: "Dresser" },
                { label: "Wardrobe" },
              ],
            },
          ],
          [
            {
              label: "Office",
              items: [
                { label: "Bookcase" },
                { label: "Cabinet" },
                { label: "Chair" },
                { label: "Desk" },
                { label: "Executive Chair" },
              ],
            },
          ],
        ],
      },
      {
        label: "Electronics",
        icon: "pi pi-mobile",
        items: [
          [
            {
              label: "Computer",
              items: [
                { label: "Monitor" },
                { label: "Mouse" },
                { label: "Notebook" },
                { label: "Keyboard" },
                { label: "Printer" },
                { label: "Storage" },
              ],
            },
          ],
          [
            {
              label: "Home Theater",
              items: [
                { label: "Projector" },
                { label: "Speakers" },
                { label: "TVs" },
              ],
            },
          ],
          [
            {
              label: "Gaming",
              items: [
                { label: "Accessories" },
                { label: "Console" },
                { label: "PC" },
                { label: "Video Games" },
              ],
            },
          ],
          [
            {
              label: "Appliances",
              items: [
                { label: "Coffee Machine" },
                { label: "Fridge" },
                { label: "Oven" },
                { label: "Vaccum Cleaner" },
                { label: "Washing Machine" },
              ],
            },
          ],
        ],
      },
      {
        label: "Sports",
        icon: "pi pi-clock",
        items: [
          [
            {
              label: "Football",
              items: [
                { label: "Kits" },
                { label: "Shoes" },
                { label: "Shorts" },
                { label: "Training" },
              ],
            },
          ],
          [
            {
              label: "Running",
              items: [
                { label: "Accessories" },
                { label: "Shoes" },
                { label: "T-Shirts" },
                { label: "Shorts" },
              ],
            },
          ],
          [
            {
              label: "Swimming",
              items: [
                { label: "Kickboard" },
                { label: "Nose Clip" },
                { label: "Swimsuits" },
                { label: "Paddles" },
              ],
            },
          ],
          [
            {
              label: "Tennis",
              items: [
                { label: "Balls" },
                { label: "Rackets" },
                { label: "Shoes" },
                { label: "Training" },
              ],
            },
          ],
        ],
      },
    ];
  }
}
```

## Inputs

| Name           | Type           | Default    | Description                                                                          |
| -------------- | -------------- | ---------- | ------------------------------------------------------------------------------------ |
| model          | MegaMenuItem[] | -          | An array of menuitems.                                                               |
| orientation    | string         | horizontal | Defines the orientation.                                                             |
| id             | string         | -          | Current id state as a string.                                                        |
| ariaLabel      | string         | -          | Defines a string value that labels an interactive element.                           |
| ariaLabelledBy | string         | -          | Identifier of the underlying input element.                                          |
| breakpoint     | string         | 960px      | The breakpoint to define the maximum width boundary.                                 |
| scrollHeight   | string         | 20rem      | Height of the viewport, a scrollbar is defined if height of list exceeds this value. |
| disabled       | boolean        | false      | When present, it specifies that the component should be disabled.                    |
| tabindex       | number         | 0          | Index of the element in tabbing order.                                               |

## Templates

| Name        | Type                                     | Description                                          |
| ----------- | ---------------------------------------- | ---------------------------------------------------- |
| start       | TemplateRef<void>                        | Defines template option for start.                   |
| end         | TemplateRef<void>                        | Defines template option for end.                     |
| menuicon    | TemplateRef<void>                        | Defines template option for menu icon.               |
| submenuicon | TemplateRef<void>                        | Defines template option for submenu icon.            |
| item        | TemplateRef<MegaMenuItemTemplateContext> | Custom item template.                                |
| button      | TemplateRef<void>                        | Custom menu button template on responsive mode.      |
| buttonicon  | TemplateRef<void>                        | Custom menu button icon template on responsive mode. |

**Full API & more examples:** https://primeng.org/megamenu
