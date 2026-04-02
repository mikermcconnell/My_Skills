---
name: commit-conventions
description: Write consistent, semantic commit messages following conventional commits format. Use when creating git commits, reviewing commit messages, or discussing version control practices.
---

# Commit Conventions

## Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

## Types

| Type | When to Use |
|------|-------------|
| `feat` | New feature for the user |
| `fix` | Bug fix for the user |
| `docs` | Documentation only changes |
| `style` | Formatting, missing semicolons (no code change) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or correcting tests |
| `chore` | Build process, dependencies, tooling |

## Rules

1. **Subject line**: Max 50 characters, imperative mood ("add" not "added")
2. **Scope**: Optional, describes the section of codebase (e.g., `auth`, `planner`, `api`)
3. **Body**: Wrap at 72 characters, explain *what* and *why* (not *how*)
4. **Breaking changes**: Add `BREAKING CHANGE:` in footer or `!` after type

## Examples

### Simple feature
```
feat(auth): add Google Sign-In button
```

### Bug fix with context
```
fix(planner): prevent duplicate activities on drag

Activities were being duplicated when dragged between days
due to missing cleanup in the drop handler.

Closes #142
```

### Breaking change
```
feat(api)!: change trip response format

BREAKING CHANGE: Trip objects now use camelCase keys instead of snake_case
```

### Refactor
```
refactor(stores): extract Firebase logic into services

Move Firestore operations from tripStore to tripFirestoreService
for better separation of concerns.
```

## Anti-Patterns to Avoid

- "Fixed stuff" - too vague
- "WIP" - don't commit incomplete work
- "Updates" - says nothing
- Past tense ("added feature") - use imperative
- Multiple unrelated changes in one commit
