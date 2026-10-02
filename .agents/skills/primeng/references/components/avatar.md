# Avatar (`p-avatar`)

Avatar represents people using icons, labels and images.

**Import:**

```ts
import { AvatarModule } from "primeng/avatar";
```

## Example

```typescript
import { Component } from "@angular/core";
import { AvatarModule } from "primeng/avatar";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-avatar-group>
        <p-avatar
          image="https://primefaces.org/cdn/primeng/images/demo/avatar/amyelsner.png"
          size="large"
          shape="circle"
        />
        <p-avatar
          image="https://primefaces.org/cdn/primeng/images/demo/avatar/asiyajavayant.png"
          size="large"
          shape="circle"
        />
        <p-avatar
          image="https://primefaces.org/cdn/primeng/images/demo/avatar/onyamalimba.png"
          size="large"
          shape="circle"
        />
        <p-avatar
          image="https://primefaces.org/cdn/primeng/images/demo/avatar/ionibowcher.png"
          size="large"
          shape="circle"
        />
        <p-avatar
          image="https://primefaces.org/cdn/primeng/images/demo/avatar/xuxuefeng.png"
          size="large"
          shape="circle"
        />
        <p-avatar label="+2" shape="circle" size="large" />
      </p-avatar-group>
    </div>
  `,
  standalone: true,
  imports: [AvatarModule],
})
export class AvatarAvatargroupDemo {}
```

## Inputs

| Name           | Type                            | Default | Description                                                                                                     |
| -------------- | ------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| label          | string                          | -       | Defines the text to display.                                                                                    |
| icon           | string                          | -       | Defines the icon to display.                                                                                    |
| image          | string                          | -       | Defines the image to display.                                                                                   |
| size           | "large" \| "xlarge" \| "normal" | normal  | Size of the element.                                                                                            |
| shape          | "circle" \| "square"            | square  | Shape of the element.                                                                                           |
| ariaLabel      | string                          | -       | Establishes a string value that labels the component.                                                           |
| ariaLabelledBy | string                          | -       | Establishes relationships between the component and label(s) where its value should be one or more element IDs. |

## Outputs

| Name         | Parameters   | Description                                                             |
| ------------ | ------------ | ----------------------------------------------------------------------- |
| onImageError | event: Event | This event is triggered if an error occurs while loading an image file. |

**Full API & more examples:** https://primeng.org/avatar
