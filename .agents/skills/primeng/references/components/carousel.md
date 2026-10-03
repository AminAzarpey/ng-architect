# Carousel (`p-carousel`)

Carousel is a content slider featuring various customization options.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { CarouselModule } from "primeng/carousel";
import { TagModule } from "primeng/tag";
```

## Example

```typescript
import { Component, OnInit, inject, signal } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { CarouselModule } from "primeng/carousel";
import { TagModule } from "primeng/tag";
import { ProductService } from "@/service/productservice";
import { Product } from "@/domain/product";

@Component({
  template: `
    <div class="card">
      <p-carousel
        [value]="products()"
        [numVisible]="3"
        [numScroll]="3"
        [circular]="false"
        [responsiveOptions]="responsiveOptions"
      >
        <ng-template let-product #item>
          <div class="border border-surface rounded-border m-2 p-4">
            <div class="mb-4">
              <div class="relative mx-auto">
                <img
                  src="https://primefaces.org/cdn/primeng/images/demo/product/{{
                    product.image
                  }}"
                  [alt]="product.name"
                  class="w-full rounded-border"
                />
                <p-tag
                  [value]="product.inventoryStatus"
                  [severity]="getSeverity(product.inventoryStatus)"
                  class="absolute dark:!bg-surface-900"
                  [ngStyle]="{ 'left.px': 5, 'top.px': 5 }"
                />
              </div>
            </div>
            <div class="mb-4 font-medium">{{ product.name }}</div>
            <div class="flex justify-between items-center">
              <div class="mt-0 font-semibold text-xl">
                {{ "$" + product.price }}
              </div>
              <span>
                <p-button
                  icon="pi pi-heart"
                  severity="secondary"
                  [outlined]="true"
                />
                <p-button icon="pi pi-shopping-cart" styleClass="ml-2" />
              </span>
            </div>
          </div>
        </ng-template>
      </p-carousel>
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, CarouselModule, TagModule],
  providers: [ProductService],
})
export class CarouselBasicDemo implements OnInit {
  private productService = inject(ProductService);
  products = signal<Product[]>([]);
  responsiveOptions: any[] | undefined;

  ngOnInit() {
    this.productService.getProductsSmall().then((data) => {
      this.products.set(data.slice(0, 9));
    });
    this.responsiveOptions = [
      {
        breakpoint: "1400px",
        numVisible: 2,
        numScroll: 1,
      },
      {
        breakpoint: "1199px",
        numVisible: 3,
        numScroll: 1,
      },
      {
        breakpoint: "767px",
        numVisible: 2,
        numScroll: 1,
      },
      {
        breakpoint: "575px",
        numVisible: 1,
        numScroll: 1,
      },
    ];
  }

  getSeverity(status: string) {
    switch (status) {
      case "INSTOCK":
        return "success";
      case "LOWSTOCK":
        return "warn";
      case "OUTOFSTOCK":
        return "danger";
    }
  }
}
```

## Inputs

| Name                   | Type                        | Default    | Description                                                             |
| ---------------------- | --------------------------- | ---------- | ----------------------------------------------------------------------- |
| page                   | number                      | -          | Index of the first item.                                                |
| numVisible             | number                      | -          | Number of items per page.                                               |
| numScroll              | number                      | -          | Number of items to scroll.                                              |
| responsiveOptions      | CarouselResponsiveOptions[] | -          | An array of options for responsive design.                              |
| orientation            | "vertical" \| "horizontal"  | horizontal | Specifies the layout of the component.                                  |
| verticalViewPortHeight | string                      | 300px      | Height of the viewport in vertical layout.                              |
| contentClass           | string                      | -          | Style class of main content.                                            |
| indicatorsContentClass | string                      | -          | Style class of the indicator items.                                     |
| indicatorsContentStyle | { [klass: string]: any }    | -          | Inline style of the indicator items.                                    |
| indicatorStyleClass    | string                      | -          | Style class of the indicators.                                          |
| indicatorStyle         | { [klass: string]: any }    | -          | Style of the indicators.                                                |
| value                  | any[]                       | -          | An array of objects to display.                                         |
| circular               | boolean                     | false      | Defines if scrolling would be infinite.                                 |
| showIndicators         | boolean                     | true       | Whether to display indicator container.                                 |
| showNavigators         | boolean                     | true       | Whether to display navigation buttons in container.                     |
| autoplayInterval       | number                      | 0          | Time in milliseconds to scroll items automatically.                     |
| prevButtonProps        | ButtonProps                 | ...        | Used to pass all properties of the ButtonProps to the Button component. |
| nextButtonProps        | ButtonProps                 | ...        | Used to pass all properties of the ButtonProps to the Button component. |

## Outputs

| Name   | Parameters               | Description                      |
| ------ | ------------------------ | -------------------------------- |
| onPage | event: CarouselPageEvent | Callback to invoke after scroll. |

## Templates

| Name         | Type                                          | Description                    |
| ------------ | --------------------------------------------- | ------------------------------ |
| item         | TemplateRef<CarouselItemTemplateContext<any>> | Custom item template.          |
| header       | TemplateRef<void>                             | Custom header template.        |
| footer       | TemplateRef<void>                             | Custom footer template.        |
| previousicon | TemplateRef<void>                             | Custom previous icon template. |
| nexticon     | TemplateRef<void>                             | Custom next icon template.     |

**Full API & more examples:** https://primeng.org/carousel
