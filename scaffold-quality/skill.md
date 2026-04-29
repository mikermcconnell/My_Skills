---
name: scaffold-quality
description: One-command setup for TypeScript project quality tooling. Use when starting a new project or adding ESLint, Husky, strict TypeScript, Codex hooks, and related verification.
---

# Scaffold Quality Tooling

One-command setup for code quality tooling in any TypeScript project.

## When to Use
Run `/scaffold-quality` when starting a new TypeScript project or adding quality tooling to an existing one.

## What It Does

Sets up five layers of project-specific tooling infrastructure. Skip any layer that's already set up.

### 1. ESLint (Flat Config)
- Install: `eslint@9`, `@eslint/js@9`, `typescript-eslint`, `eslint-plugin-react-hooks@5` (if React)
- Create `eslint.config.js` with recommended rules
- Add `"lint"` script to package.json

### 2. Husky Pre-Commit Hook
- Install: `husky`
- Run `npx husky init`
- Configure `.husky/pre-commit` to run `npx tsc --noEmit`

### 3. TypeScript Strict Mode (Incremental)
- Enable `noImplicitAny: true` in tsconfig.json
- Fix any resulting errors (usually < 20 for new projects)
- Leave `strict: true` as a future goal documented in a comment

### 4. Codex Hooks (Project-Level)
- Create `.Codex/settings.json` with PostToolUse hooks:
  - `tsc --noEmit` after Write/Edit (60s timeout)
  - Related test runner if vitest/jest is present

### 5. AGENTS.md Danger Zones
- Add a Danger Zones table to `.Codex/AGENTS.md` listing high-risk files with verification commands

## Instructions

1. **Detect the project**: Read `package.json` and `tsconfig.json` to understand the stack.
2. **Check existing tooling**: Skip any layer that's already set up (e.g., if ESLint config exists, skip ESLint).
3. **Install dependencies**: Run `npm install` after adding packages.
4. **Verify**: Run `npx tsc --noEmit` and `npm run lint` to confirm everything works.
5. **Report**: List what was set up, what was skipped, and any manual steps remaining.

## Constraints
- Do NOT install Prettier (user preference — ESLint handles formatting rules)
- Do NOT enable `strict: true` directly — use incremental strictness (`noImplicitAny` first)
- Do NOT add `noUnusedLocals` or `noUnusedParameters` — these cause too many false positives during development
- Keep ESLint rules pragmatic: `no-explicit-any: off`, unused vars with `_` prefix allowed
- For React projects, detect whether it's React Native/Expo vs web-only and adjust accordingly

## Note
Coding standards (workflow orchestration, task management, core principles, accountability) live in the **global** `~/.Codex/AGENTS.md` and apply automatically to all projects. This skill only handles project-specific tooling setup.
