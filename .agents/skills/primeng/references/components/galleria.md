# Gallery (`p-galleria`)

Galleria is an advanced content gallery component.

**Import:**

```ts
import { GalleriaModule } from "primeng/galleria";
```

## Example

```typescript
import { Component, OnInit, inject } from "@angular/core";
import { GalleriaModule } from "primeng/galleria";
import { PhotoService } from "@/service/photoservice";

@Component({
  template: `
    <div class="card">
      <p-galleria
        [(value)]="images"
        [responsiveOptions]="responsiveOptions"
        [containerStyle]="{ 'max-width': '640px' }"
        [numVisible]="5"
      >
        <ng-template #item let-item>
          <img [src]="item.itemImageSrc" style="width:100%" />
        </ng-template>
        <ng-template #thumbnail let-item>
          <img [src]="item.thumbnailImageSrc" />
        </ng-template>
      </p-galleria>
    </div>
  `,
  standalone: true,
  imports: [GalleriaModule],
  providers: [PhotoService],
})
export class GalleriaBasicDemo implements OnInit {
  private photoService = inject(PhotoService);
  images: any = model([]);
  responsiveOptions: any[];

  ngOnInit() {
    this.photoService.getImages().then((images) => this.images.set(images));
  }
}
```

## Inputs

| Name                            | Type                                   | Default | Description                                                                                    |
| ------------------------------- | -------------------------------------- | ------- | ---------------------------------------------------------------------------------------------- |
| activeIndex                     | number                                 | -       | Index of the first item.                                                                       |
| fullScreen                      | boolean                                | false   | Whether to display the component on fullscreen.                                                |
| id                              | string                                 | -       | Unique identifier of the element.                                                              |
| value                           | any[]                                  | -       | An array of objects to display.                                                                |
| numVisible                      | number                                 | 3       | Number of items per page.                                                                      |
| responsiveOptions               | GalleriaResponsiveOptions[]            | -       | An array of options for responsive design.                                                     |
| showItemNavigators              | boolean                                | false   | Whether to display navigation buttons in item section.                                         |
| showThumbnailNavigators         | boolean                                | true    | Whether to display navigation buttons in thumbnail container.                                  |
| showItemNavigatorsOnHover       | boolean                                | false   | Whether to display navigation buttons on item hover.                                           |
| changeItemOnIndicatorHover      | boolean                                | false   | When enabled, item is changed on indicator hover.                                              |
| circular                        | boolean                                | false   | Defines if scrolling would be infinite.                                                        |
| autoPlay                        | boolean                                | false   | Items are displayed with a slideshow in autoPlay mode.                                         |
| shouldStopAutoplayByClick       | boolean                                | true    | When enabled, autorun should stop by click.                                                    |
| transitionInterval              | number                                 | 4000    | Time in milliseconds to scroll items.                                                          |
| showThumbnails                  | boolean                                | true    | Whether to display thumbnail container.                                                        |
| thumbnailsPosition              | "right" \| "left" \| "top" \| "bottom" | bottom  | Position of thumbnails.                                                                        |
| verticalThumbnailViewPortHeight | string                                 | 300px   | Height of the viewport in vertical thumbnail.                                                  |
| showIndicators                  | boolean                                | false   | Whether to display indicator container.                                                        |
| showIndicatorsOnItem            | boolean                                | false   | When enabled, indicator container is displayed on item container.                              |
| indicatorsPosition              | "right" \| "left" \| "top" \| "bottom" | bottom  | Position of indicators.                                                                        |
| baseZIndex                      | number                                 | 0       | Base zIndex value to use in layering.                                                          |
| maskClass                       | string                                 | -       | Style class of the mask on fullscreen mode.                                                    |
| containerClass                  | string                                 | -       | Style class of the component on fullscreen mode. Otherwise, the 'class' property can be used.  |
| containerStyle                  | { [klass: string]: any }               | -       | Inline style of the component on fullscreen mode. Otherwise, the 'style' property can be used. |
| motionOptions                   | InputSignal<MotionOptions>             | ...     | The motion options.                                                                            |
| maskMotionOptions               | InputSignal<MotionOptions>             | ...     | The mask motion options.                                                                       |
| visible                         | boolean                                | -       | Specifies the visibility of the mask on fullscreen mode.                                       |

## Outputs

| Name              | Parameters     | Description                                |
| ----------------- | -------------- | ------------------------------------------ |
| activeIndexChange | value: number  | Callback to invoke on active index change. |
| visibleChange     | value: boolean | Callback to invoke on visiblity change.    |

## Templates

| Name                    | Type                                               | Description                              |
| ----------------------- | -------------------------------------------------- | ---------------------------------------- |
| header                  | TemplateRef<void>                                  | Custom header template.                  |
| footer                  | TemplateRef<void>                                  | Custom footer template.                  |
| indicator               | TemplateRef<GalleriaIndicatorTemplateContext>      | Custom indicator template.               |
| caption                 | TemplateRef<GalleriaCaptionTemplateContext<any>>   | Custom caption template.                 |
| \_closeicon             | TemplateRef<void>                                  | Custom close icon template.              |
| \_previousthumbnailicon | TemplateRef<void>                                  | Custom previous thumbnail icon template. |
| \_nextthumbnailicon     | TemplateRef<void>                                  | Custom next thumbnail icon template.     |
| \_itempreviousicon      | TemplateRef<void>                                  | Custom item previous icon template.      |
| \_itemnexticon          | TemplateRef<void>                                  | Custom item next icon template.          |
| \_item                  | TemplateRef<GalleriaItemTemplateContext<any>>      | Custom item template.                    |
| \_thumbnail             | TemplateRef<GalleriaThumbnailTemplateContext<any>> | Custom thumbnail template.               |

**Full API & more examples:** https://primeng.org/galleria
