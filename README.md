# 🧱 ng-architect

A modern and scalable **Angular 20+ starter architecture** for building enterprise-grade ERP systems. Designed for modularity, maintainability, and productivity, this project includes a full CI-ready setup, dynamic lazy loading, Material + Tailwind hybrid UI support, and git-based changelog/versioning workflows.

---

## 🚀 Features

- ✅ **Angular 20 Standalone Architecture**
- 🧩 Modular DDD-style folder structure
- 📦 **Dynamic Component Rendering** (e.g. lazy grids, cards, panels)
- 🪝 Signal-based State & Reactive UX (ready for Angular Signals Store)
- 🎨 TailwindCSS + Angular Material integration
- 🌐 i18n ready, mock-auth included
- 🧪 Karma + Jasmine Testing + E2E scaffolding
- 📜 Conventional commits + auto-generated changelog (`release-it`)
- ✨ Prettier + ESLint + Husky + Commitizen

---

## 📁 Project Structure (DDD Friendly)

```
src/
├── app/
│   ├── core/               # services, interceptors, configuration
│   ├── features/           # feature modules, one per domain
│   ├── shared/             # shared components, directives, pipes
│   └── app.config.ts       # standalone app setup
├── assets/                 # images, translations
└── main.ts                 # bootstrap logic
```

---

## 🛠 Getting Started

```bash
# Clone the project
git clone https://github.com/AminAzarpey/ng-architect.git
cd ng-architect

# Install dependencies
npm install

# Start development server
npm run start
```

---

## ⚙️ Development Scripts

| Script            | Description                       |
| ----------------- | --------------------------------- |
| `npm run start`   | Start local dev server (with HMR) |
| `npm run build`   | Build for production              |
| `npm run test`    | Run unit tests                    |
| `npm run lint`    | Run ESLint + auto-fix             |
| `npm run format`  | Format using Prettier             |
| `npm run commit`  | Commit using Commitizen prompt    |
| `npm run release` | Bump version, generate changelog  |

---

## ✨ Git & Release Workflow

This project uses:

- **Conventional Commits** (`cz`, `commitizen`, `commitlint`)
- **Release-it** with `@release-it/conventional-changelog`

### Example Release Flow

```bash
# Stage and commit as usual (use `npm run commit`)
npm run commit

# Run release with changelog, version bump, and GitHub tag
npm run release
```

> This will update the version, modify `CHANGELOG.md`, and push a GitHub release tag.

---

## 🧪 Testing

```bash
npm run test       # run unit tests (Karma + Jasmine)
```

> Cypress or Playwright can be added for E2E testing.

---

## 🧰 Tooling Overview

| Tool        | Purpose                     |
| ----------- | --------------------------- |
| Angular 20  | Main front-end framework    |
| TailwindCSS | Utility-first styling       |
| Material    | UI Components & UX patterns |
| ESLint      | Static code analysis        |
| Prettier    | Code formatting             |
| Husky       | Git hooks                   |
| Commitizen  | Conventional commits        |
| Release-it  | Versioning & changelog      |

---

## 📒 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for commit-based release notes.

---

## 📜 License

MIT © [Amin Azarpey](https://github.com/AminAzarpey)
