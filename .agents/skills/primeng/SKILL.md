---
name: primeng
description: >-
  Build and review Angular interfaces with PrimeNG components, directives,
  forms, overlays, services, themes, PrimeIcons, and Tailwind integration.
  Use for p-* components, providePrimeNG, design tokens, passthrough,
  accessibility, or PrimeNG migrations. Check the installed version;
  the bundled documentation supports this project's v21 stack.
license: MIT
metadata:
  author: Adapted from the user-supplied PrimeNG documentation
  version: "2.0"
  targets: PrimeNG v21
  documentation_snapshot: "2026-06-04"
---

# PrimeNG development

Use this skill to implement or review PrimeNG presentation code. Inspect `package.json`, application providers, and style entry points before changing setup. This repository uses Angular 21, PrimeNG 21.1.10, Aura through `@primeuix/themes`, Angular Material, and Tailwind CSS together. PrimeNG 21 is MIT-licensed and needs no activation key. Preserve that choice unless the user requests a version change.

## Find the relevant reference

The supplied LLM documentation is split into 115 sections. Read [the source index](references/source-index.md) to locate the needed component, directive, guide, or migration, then load only relevant sections. Each section preserves its original text. Read [compatibility guidance](references/compatibility.md) when a historical example conflicts with the installed API.

Existing focused references remain available for quick patterns:

| Work | Reference |
| --- | --- |
| Providers and setup | [Installation](references/installation.md), [configuration](references/configuration.md) |
| Tokens, presets, density, dark mode | [Theming](references/theming.md) |
| Tailwind, CSS layers, unstyled mode, passthrough | [Styling integration](references/styling-integration.md) |
| Toast, confirmations, dynamic dialogs | [Services](references/services.md) |
| Icons and bidirectional layouts | [Icons](references/icons.md), [RTL](references/rtl.md) |
| Keyboard, ARIA, focus, accessible names | [Accessibility](references/accessibility.md) |
| Behaviors on native elements | [Directives](references/directives.md) |

For example, [Button](references/source/angular-button-component.md), [Table](references/source/angular-table-component.md), [Select](references/source/angular-select-component.md), and [Dialog](references/source/angular-dialog-component.md) contain full supplied examples and API details. Other topics are routed through the index.

## Implement the feature

- Keep PrimeNG imports in presentation components and shared UI wrappers. Domain models and application use cases stay independent of UI libraries. Material and Tailwind remain selectable alongside PrimeNG; choose local feature imports rather than replacing another library.
- Import only the components/directives or modules the standalone component uses. Check installed declarations when an export, selector, input, output, slot, or passthrough key is uncertain.
- Configure `providePrimeNG` once with `theme: { preset: Aura }`. Prefer design tokens and `definePreset` for theming, supported `pt` sections for internal attributes or classes, and avoid broad overrides of component internals.
- Use native CSS animation guidance from the snapshot. Do not add Angular's legacy animation package/provider solely because an older snippet includes it; verify an actual component requirement first.
- Prefer named template references such as `<ng-template #body>` for documented slots. `pTemplate` appears in historical examples and is deprecated in v21; use modern syntax for new code.
- Keep the feature's existing Angular form strategy. Import the appropriate forms support, handle disabled/loading/error states, and confirm value and event types against the component API.
- For service-backed UI, provide both the service and its host: `MessageService` with `<p-toast>`, `ConfirmationService` with `<p-confirmdialog>`, or `DialogService` for dynamic dialogs. Choose provider scope to match the consuming feature's lifecycle.
- Use Tailwind for layout and spacing alongside component themes. Align dark-mode selectors, CSS layer ordering, overlay stacking, typography, and focus treatment across libraries. Check utilities against both libraries when changing global CSS.

## Verify the result

Run relevant types, lint, and tests through the pinned toolchain, and build when application code or configuration changes. For interactive controls, verify visible behavior, keyboard operation, accessible names, focus restoration, responsive layout, and form validation in the browser. Compilation alone does not establish accessibility or backend integration.

## Refresh the snapshot

When the user supplies updated LLM documentation, run:

```sh
python3 .agents/skills/primeng/scripts/import_llms.py <path-to-new-documentation>
```

The importer preserves original bytes across topic files, regenerates the index and checksum manifest, and refuses to overwrite edited generated references. Review compatibility guidance and targeted examples after importing; the generation date does not prove every example matches the installed version.
