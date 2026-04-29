---
name: pm-review
description: Review implementation plans against the Investing app's product vision and architectural principles. Acts as a project-specific PM checkpoint before significant work. Use when working in this codebase and reviewing plans for complex features, architecture changes, or product scope decisions for this project, or when `/pm-review` is invoked.
---

# PM Review Skill

Review implementation plans against the app's product vision and architectural principles.

## Triggers

- User asks for "PM review", "product review", "review this plan"
- `/pm-review` command
- Before implementing complex features (proactive use during planning)

## Purpose

Ensures plans align with:
1. **Product Vision** — Does the feature fit the app's purpose?
2. **User Workflows** — Does it support core user journeys?
3. **Architectural Principles** — Does it follow established patterns?
4. **Feature Priorities** — Is this the right thing to build now?
5. **Anti-Patterns** — Are we avoiding what the app is NOT supposed to do?

## Workflow

### 1. Gather Context

| Document | Location | Purpose |
|----------|----------|---------|
| Product Vision | `docs/PRODUCT_VISION.md` | What the app is/isn't |
| Project Guidelines | `AGENTS.md` | Coding standards, patterns |
| Strategy Notes | `docs/AI_PICKS_STRATEGY_NOTES.md` | AI strategy data |

### 2. Review Against Criteria

#### Vision Alignment
- Does this fit the app's core purpose (validation + tracking)?
- Does it support a defined user persona?
- Does it avoid anti-patterns (trade execution, financial advice, AI generation)?

#### Architectural Alignment
- Is it implemented web-first (Flask routes + templates)?
- Does it follow simplicity principle (minimum complexity)?
- Does it respect Firebase/SQLite dual-mode storage?

#### Scope Appropriateness
- Is the scope focused (not adding "just in case" features)?
- Are changes localized (not refactoring unrelated code)?

### 3. Output Structured Review

```markdown
## PM Review: [Feature Name]

### Vision Alignment
- [x] Fits core purpose: [Yes/No]
- [x] Supports user workflow: [Which]
- [x] Avoids anti-patterns: [Yes/No]

### Architectural Alignment
- [x] Web-first: [Yes/No]
- [x] Follows patterns: [Yes/No]
- [x] Appropriate complexity: [Yes/No]

### Concerns
1. [Specific issue]

### Recommendation
**[APPROVE / APPROVE WITH CHANGES / NEEDS DISCUSSION / REJECT]**
```

## Recommendation Levels

| Level | Meaning |
|-------|---------|
| **APPROVE** | Aligns with vision and architecture |
| **APPROVE WITH CHANGES** | Minor adjustments needed |
| **NEEDS DISCUSSION** | Significant questions |
| **REJECT** | Conflicts with product vision |

## Common Red Flags

- Adding trade execution or brokerage integration
- Creating abstractions before 3+ use cases
- Refactoring working code that wasn't asked to change
- Building Tier 4 features when Tier 1 needs work
