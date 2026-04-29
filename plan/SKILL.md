---
name: plan
description: Create implementation plans for changes in the Investing repo, with automatic PM review for complex work. Use when working in this codebase and the user wants to plan, design, architect, or scope a non-trivial feature, route, data change, or subsystem update for this project.
---

# Plan Skill (with Auto PM Review)

Create implementation plans for features, automatically triggering PM review for complex changes.

## Triggers

- User asks to "plan", "design", "architect", or "figure out how to implement"
- `/plan` command
- Entering plan mode for non-trivial features

## Workflow

### 1. Understand the Request

Clarify scope: what feature, which user workflow, affected codebase areas.

### 2. Explore the Codebase

| If Feature Involves | Explore |
|---------------------|---------|
| New route/page | `web/routes/`, `web/templates/`, similar existing routes |
| Data storage | `src/data/firestore_service.py`, existing collections |
| AI picks | `src/ai_picks/`, strategy implementations |
| Portfolio | `src/portfolio/`, tracker, performance modules |
| Analysis | `src/analysis/`, technical indicators, charts |
| Alerts/monitoring | `src/monitor/`, existing alert patterns |

### 3. Create Implementation Plan

```markdown
## Implementation Plan: [Feature Name]

### Summary
[1-2 sentences]

### Affected Files
- `web/routes/xxx.py` - [what changes]

### Steps
1. [Step 1]
2. [Step 2]

### Patterns to Follow
- [Existing pattern to replicate]

### Open Questions
- [Decisions needed]
```

### 4. Auto-Trigger PM Review

Run `/pm-review` if ANY of these are true:

| Condition | Reason |
|-----------|--------|
| Plan affects 3+ files | Multi-file changes need vision check |
| Plan adds new route or template | New UI surfaces need alignment check |
| Plan adds database collection | Data model changes are significant |
| Plan creates new module/class | Abstraction decisions need review |
| Plan touches Tier 1 features | Core features need extra scrutiny |

### 5. Wait for Approval

Do not proceed with implementation until user confirms.

## Skip PM Review When

- Single-file bug fixes
- Minor text/style changes
- Adding a single function to existing module
- Changes explicitly scoped as "quick fix"
