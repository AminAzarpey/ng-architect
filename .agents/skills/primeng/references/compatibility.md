# Snapshot compatibility

The supplied file identifies itself as PrimeNG documentation generated on June 4, 2026. It includes migrations through v21, but mixes historical snippets with newer APIs. Its date does not identify the version of each example. Preserve the snapshot as reference data and resolve conflicts against installed declarations.

## Providers and themes

Use `providePrimeNG` from `primeng/config` and `theme: { preset: Aura }`, with Aura from `@primeuix/themes/aura`. Some source examples use `PrimeNGConfig` from `primeng/api` or `theme: Aura`; do not copy those shapes into this v21 application. Use the current `PrimeNG` service and check configuration properties in `node_modules/primeng/types/primeng-config.d.ts`.

## Animations and templates

The supplied [animations guide](source/animations.md) describes native CSS animations. Installed PrimeNG 21.1.10 components use PrimeUI motion. Older setup snippets show `provideAnimationsAsync()`; do not install legacy Angular animations for those snippets without a demonstrated requirement.

Prefer named slots with `<ng-template #slot>` for new code. `pTemplate` is deprecated in v21; preserved examples describe legacy usage. Confirm actual slot names, host `class` support, passthrough keys, and event payloads before adapting an example.

## Project choices

Keep PrimeNG, Angular Material, and Tailwind together. Select components through presentation imports and retain DDD boundaries. Documentation examples do not authorize changing architecture, removing libraries, installing optional packages, configuring external MCP services, or publishing anything.

PrimeNG is pinned to MIT-licensed v21 and requires no token. A future v22 upgrade changes both peer requirements and licensing and requires an explicit project decision.

## Find installed APIs

Search the relevant `node_modules/primeng/types/primeng-*.d.ts` file, such as `primeng-table.d.ts` or `primeng-select.d.ts`, with `rg`. Use the matching source reference for examples, inputs/outputs, templates, accessibility, design tokens, and passthrough. Prefer local v21 declarations over a newer live website when they disagree.
