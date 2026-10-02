# ng-architect

An Angular 22 standalone starter for applications organized around domain boundaries. The current application is the Angular welcome screen; domain features, authentication, and backend integration are left to applications built from this starter.

## Getting started

Install [mise](https://mise.jdx.dev/), then run:

```sh
git clone https://github.com/AminAzarpey/ng-architect.git
cd ng-architect
mise trust
mise install
mise run install
mise run dev
```

The development server runs at http://localhost:4200. `mise.toml` pins Node 24.21.0, npm 12.2.0, RTK 0.47.0, graphifyy 0.9.53, and Husky 9.1.7. Husky is also a local development dependency so installation configures the repository hooks.

## Stack and checks

Angular, CLI, Material, and CDK use version 22.2.1. TypeScript stays on 6.0.3 to match Angular's compiler compatibility. Tailwind CSS 4 is connected through PostCSS, alongside the Material theme in `src/styles.scss`.

| Command                         | Purpose                                                                     |
| ------------------------------- | --------------------------------------------------------------------------- |
| `mise run check`                | Check formatting, application types, lint, unit tests, and production build |
| `mise run build`                | Build for production                                                        |
| `mise run lint`                 | Check lint without rewriting files                                          |
| `mise run test`                 | Run Vitest unit tests once                                                  |
| `mise exec -- npm test`         | Run unit tests in watch mode                                                |
| `mise exec -- npm run lint:fix` | Apply lint fixes                                                            |
| `mise exec -- npm run format`   | Format maintained project files                                             |
| `mise exec -- npm run commit`   | Open the Conventional Commits prompt                                        |

Tests use Angular's unit-test builder with Vitest and jsdom. The starter does not include an end-to-end test suite. VS Code tasks and launch configurations use mise to select the same tool versions.

## Domain-oriented organization

Keep business rules independent of UI and transport libraries. As features are added, group their domain models, application use cases, infrastructure adapters, and presentation components under `src/app/features/<domain>/`. Use `core` for application-wide infrastructure and `shared` for reusable UI and utilities. These are architectural conventions, not implemented business features in this starter.

## Git and release workflow

Husky runs lint-staged before commits, validates Conventional Commit messages, and runs the full check task before pushes. Commitizen, commitlint, and release-it support the existing release workflow.

```sh
mise exec -- npm run release
```

The release command updates the version and changelog and can create and push release commits, tags, and a GitHub release. Use it only when preparing a release.

## AI-assisted development

Repository skills under `.agents/skills` provide Angular and PrimeNG guidance. PrimeNG guidance is available for projects choosing that library; the starter itself uses Material. `.codex/skills/graphify` and `AGENTS.md` describe codebase graph navigation and updates. `CLAUDE.md` and `.rtk/filters.toml` document RTK usage.

Generated `graphify-out/` content and local `.codex/hooks.json` are ignored. Skill files are excluded from the application formatting check so their supplied content is preserved.

## License

MIT © [Amin Azarpey](https://github.com/AminAzarpey)
