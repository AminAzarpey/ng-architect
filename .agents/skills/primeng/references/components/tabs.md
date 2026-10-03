# Tabs (`p-tabs`)

Tabs is a container component to group content with tabs.

**Import:**

```ts
import { TabsModule } from "primeng/tabs";
```

## Example

```typescript
import { Component } from "@angular/core";
import { TabsModule } from "primeng/tabs";

@Component({
  template: `
    <div class="card">
      <p-tabs value="0">
        <p-tablist>
          <p-tab value="0">Header I</p-tab>
          <p-tab value="1">Header II</p-tab>
          <p-tab value="2">Header III</p-tab>
        </p-tablist>
        <p-tabpanels>
          <p-tabpanel value="0">
            <p class="m-0">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
              reprehenderit in voluptate velit esse cillum dolore eu fugiat
              nulla pariatur. Excepteur sint occaecat cupidatat non proident,
              sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
          </p-tabpanel>
          <p-tabpanel value="1">
            <p class="m-0">
              Sed ut perspiciatis unde omnis iste natus error sit voluptatem
              accusantium doloremque laudantium, totam rem aperiam, eaque ipsa
              quae ab illo inventore veritatis et quasi architecto beatae vitae
              dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit
              aspernatur aut odit aut fugit, sed quia consequuntur magni dolores
              eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci
              velit, sed quia non numquam eius modi.
            </p>
          </p-tabpanel>
          <p-tabpanel value="2">
            <p class="m-0">
              At vero eos et accusamus et iusto odio dignissimos ducimus qui
              blanditiis praesentium voluptatum deleniti atque corrupti quos
              dolores et quas molestias excepturi sint occaecati cupiditate non
              provident, similique sunt in culpa qui officia deserunt mollitia
              animi, id est laborum et dolorum fuga. Et harum quidem rerum
              facilis est et expedita distinctio. Nam libero tempore, cum soluta
              nobis est eligendi optio cumque nihil impedit quo minus.
            </p>
          </p-tabpanel>
        </p-tabpanels>
      </p-tabs>
    </div>
  `,
  standalone: true,
  imports: [TabsModule],
})
export class TabsBasicDemo {}
```

## Inputs

| Name           | Type                                       | Default   | Description                                                                    |
| -------------- | ------------------------------------------ | --------- | ------------------------------------------------------------------------------ |
| value          | ModelSignal<string \| number>              | undefined | Value of the active tab.                                                       |
| scrollable     | InputSignalWithTransform<boolean, unknown> | false     | When specified, enables horizontal and/or vertical scrolling.                  |
| lazy           | InputSignalWithTransform<boolean, unknown> | false     | When enabled, tabs are not rendered until activation.                          |
| selectOnFocus  | InputSignalWithTransform<boolean, unknown> | false     | When enabled, the focused tab is activated.                                    |
| showNavigators | InputSignalWithTransform<boolean, unknown> | true      | Whether to display navigation buttons in container when scrollable is enabled. |
| tabindex       | InputSignalWithTransform<number, unknown>  | 0         | Tabindex of the tab buttons.                                                   |

**Full API & more examples:** https://primeng.org/tabs
