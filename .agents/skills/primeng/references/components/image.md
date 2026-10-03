# Image (`p-image`)

Displays an image with preview and tranformation options.

**Import:**

```ts
import { ImageModule } from "primeng/image";
```

## Example

```typescript
import { Component } from "@angular/core";
import { ImageModule } from "primeng/image";

@Component({
  template: `
    <div class="card flex justify-center">
      <p-image
        src="https://primefaces.org/cdn/primeng/images/galleria/galleria10.jpg"
        alt="Image"
        width="250"
      />
    </div>
  `,
  standalone: true,
  imports: [ImageModule],
})
export class ImageBasicDemo {}
```

## Inputs

| Name                | Type                       | Default         | Description                                                                                                                                                                                                                                          |
| ------------------- | -------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| imageClass          | string                     | -               | Style class of the image element.                                                                                                                                                                                                                    |
| imageStyle          | { [klass: string]: any }   | -               | Inline style of the image element.                                                                                                                                                                                                                   |
| src                 | string \| SafeUrl          | -               | The source path for the main image.                                                                                                                                                                                                                  |
| srcSet              | string \| SafeUrl          | -               | The srcset definition for the main image.                                                                                                                                                                                                            |
| sizes               | string                     | -               | The sizes definition for the main image.                                                                                                                                                                                                             |
| previewImageSrc     | string \| SafeUrl          | -               | The source path for the preview image.                                                                                                                                                                                                               |
| previewImageSrcSet  | string \| SafeUrl          | -               | The srcset definition for the preview image.                                                                                                                                                                                                         |
| previewImageSizes   | string                     | -               | The sizes definition for the preview image.                                                                                                                                                                                                          |
| alt                 | string                     | -               | Attribute of the preview image element.                                                                                                                                                                                                              |
| width               | string                     | -               | Attribute of the image element.                                                                                                                                                                                                                      |
| height              | string                     | -               | Attribute of the image element.                                                                                                                                                                                                                      |
| loading             | "eager" \| "lazy"          | -               | Attribute of the image element.                                                                                                                                                                                                                      |
| preview             | boolean                    | false           | Controls the preview functionality.                                                                                                                                                                                                                  |
| modalEnterAnimation | InputSignal<string>        | 'p-modal-enter' | Enter animation class name of modal.                                                                                                                                                                                                                 |
| modalLeaveAnimation | InputSignal<string>        | 'p-modal-leave' | Leave animation class name of modal.                                                                                                                                                                                                                 |
| appendTo            | InputSignal<any>           | 'self'          | Target element to attach the overlay, valid values are "body" or a local ng-template variable of another element (note: use binding with brackets for template variables, e.g. [appendTo]="mydiv" for a div element having #mydiv as variable name). |
| maskMotionOptions   | InputSignal<MotionOptions> | ...             | The motion options for the mask.                                                                                                                                                                                                                     |
| motionOptions       | InputSignal<MotionOptions> | ...             | The motion options.                                                                                                                                                                                                                                  |

## Outputs

| Name         | Parameters   | Description                                                             |
| ------------ | ------------ | ----------------------------------------------------------------------- |
| onShow       | value: any   | Triggered when the preview overlay is shown.                            |
| onHide       | value: any   | Triggered when the preview overlay is hidden.                           |
| onImageError | event: Event | This event is triggered if an error occurs while loading an image file. |

## Templates

| Name            | Type                                     | Description                        |
| --------------- | ---------------------------------------- | ---------------------------------- |
| indicator       | TemplateRef<void>                        | Custom indicator template.         |
| rotaterighticon | TemplateRef<void>                        | Custom rotate right icon template. |
| rotatelefticon  | TemplateRef<void>                        | Custom rotate left icon template.  |
| zoomouticon     | TemplateRef<void>                        | Custom zoom out icon template.     |
| zoominicon      | TemplateRef<void>                        | Custom zoom in icon template.      |
| closeicon       | TemplateRef<void>                        | Custom close icon template.        |
| preview         | TemplateRef<ImagePreviewTemplateContext> | Custom preview template.           |
| image           | TemplateRef<ImageImageTemplateContext>   | Custom image template.             |

**Full API & more examples:** https://primeng.org/image
