# PrimeNG license choice

This project pins **PrimeNG 21.1.10**, the MIT-licensed release line. No PrimeUI account, license key, token, or activation step is needed. The [PrimeUI Community terms](https://primeui.dev/licenses/community) explicitly identify PrimeNG 21 and earlier as MIT-licensed versions.

PrimeNG 22 introduced the Community/Commercial licensing model and requires an issued license key even for eligible Community users. We selected v21 to keep this open-source starter key-free. Future upgrades to v22 or later must revisit that decision rather than silently introduce a key requirement.

## Compatible versions

PrimeNG 21 declares Angular and CDK 21 peers. The project therefore uses Angular 21.2.25, CLI/build 21.2.24, Material/CDK 21.2.14, and PrimeUI themes 2.0.3. TypeScript 5.9.3 and Vitest 4.1.11 satisfy the Angular 21 build requirements. Node/npm remain managed by mise.

## Development and builds

Run `mise run dev`, `mise run build`, and `mise run check` normally. They invoke Angular CLI directly. The former license environment launcher and its example key file have been removed. An existing local `.env.local` is preserved and ignored, but is no longer read for PrimeNG activation.

Angular Material and Tailwind CSS remain available alongside PrimeNG. Features choose components through local standalone imports; see [UI library choices](UI-LIBRARIES.md).

The installed `node_modules/primeng/LICENSE.md` contains the package's MIT terms. Retain required license notices when distributing dependencies. See [PrimeNG 21 setup](https://v21.primeng.org/installation).
