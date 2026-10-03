# Scroll Panel (`p-scrollpanel`)

ScrollPanel is a cross browser, lightweight and skinnable alternative to native browser scrollbar.

**Import:**

```ts
import { ScrollPanelModule } from "primeng/scrollpanel";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ScrollPanelModule } from "primeng/scrollpanel";

@Component({
  template: `
    <div class="card">
      <p-scrollpanel [style]="{ width: '100%', height: '150px' }">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem
          accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae
          ab illo inventore veritatis et quasi architecto beatae vitae dicta
          sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit
          aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos
          qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit,
          sed quia non numquam eius modi.
        </p>
        <p class="m-0">
          At vero eos et accusamus et iusto odio dignissimos ducimus qui
          blanditiis praesentium voluptatum deleniti atque corrupti quos dolores
          et quas molestias excepturi sint occaecati cupiditate non provident,
          similique sunt in culpa qui officia deserunt mollitia animi, id est
          laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita
          distinctio. Nam libero tempore, cum soluta nobis est eligendi optio
          cumque nihil impedit quo minus.
        </p>
      </p-scrollpanel>
    </div>
  `,
  standalone: true,
  imports: [ScrollPanelModule],
})
export class ScrollpanelBasicDemo {}
```

## Inputs

| Name | Type   | Default | Description                                                      |
| ---- | ------ | ------- | ---------------------------------------------------------------- |
| step | number | 5       | Step factor to scroll the content while pressing the arrow keys. |

## Templates

| Name    | Type              | Description              |
| ------- | ----------------- | ------------------------ |
| content | TemplateRef<void> | Custom content template. |

## Methods

| Name      | Parameters        | Return Type | Description                                       |
| --------- | ----------------- | ----------- | ------------------------------------------------- |
| scrollTop | scrollTop: number | void        | Scrolls the top location to the given value.      |
| refresh   |                   | void        | Refreshes the position and size of the scrollbar. |

**Full API & more examples:** https://primeng.org/scrollpanel
