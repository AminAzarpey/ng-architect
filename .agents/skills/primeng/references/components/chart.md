# Chart (`p-chart`)

Chart components are based on Charts.js 3.3.2+, an open source HTML5 based charting library.

**Import:**

```ts
import { ChartModule } from "primeng/chart";
```

## Example

```typescript
import { Component, OnInit, inject } from "@angular/core";
import { ChartModule } from "primeng/chart";

@Component({
  template: `
    <div class="card">
      <p-chart type="bar" [data]="basicData" [options]="basicOptions" />
    </div>
  `,
  standalone: true,
  imports: [ChartModule],
})
export class ChartBasicDemo implements OnInit {
  basicData: any;
  basicOptions: any;
  platformId = inject(PLATFORM_ID);
  configService = inject(AppConfigService);
  designerService = inject(DesignerService);

  ngOnInit() {
    this.initChart();
  }

  initChart() {
    if (isPlatformBrowser(this.platformId)) {
      const documentStyle = getComputedStyle(document.documentElement);
      const textColor = documentStyle.getPropertyValue("--p-text-color");
      const textColorSecondary = documentStyle.getPropertyValue(
        "--p-text-muted-color",
      );
      const surfaceBorder = documentStyle.getPropertyValue(
        "--p-content-border-color",
      );

      this.basicData = {
        labels: ["Q1", "Q2", "Q3", "Q4"],
        datasets: [
          {
            label: "Sales",
            data: [540, 325, 702, 620],
            backgroundColor: [
              "rgba(249, 115, 22, 0.2)",
              "rgba(6, 182, 212, 0.2)",
              "rgb(107, 114, 128, 0.2)",
              "rgba(139, 92, 246, 0.2)",
            ],
            borderColor: [
              "rgb(249, 115, 22)",
              "rgb(6, 182, 212)",
              "rgb(107, 114, 128)",
              "rgb(139, 92, 246)",
            ],
            borderWidth: 1,
          },
        ],
      };

      this.basicOptions = {
        maintainAspectRatio: false,
        aspectRatio: 0.8,
        plugins: {
          legend: {
            labels: {
              color: textColor,
            },
          },
        },
        scales: {
          x: {
            ticks: {
              color: textColorSecondary,
            },
            grid: {
              color: surfaceBorder,
            },
          },
          y: {
            beginAtZero: true,
            ticks: {
              color: textColorSecondary,
            },
            grid: {
              color: surfaceBorder,
            },
          },
        },
      };
      this.cd.markForCheck();
    }
  }
}
```

**Full API & more examples:** https://primeng.org/chart
