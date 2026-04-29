---
name: verify
description: Run the Investing project's verification suite with smart defaults and summarize the results. Use when working in this codebase and the user asks to verify, check the code, run tests, lint, or confirm changes after editing this project.
---

# Verify Skill

Run the project's verification suite with smart defaults and summarize results.

## Triggers

- User asks to "verify", "check the code", "run tests", "lint check"
- `/verify` command
- After making code changes (proactive use)

## Workflow

### 1. Run Verification

| Situation | Command |
|-----------|---------|
| Quick check after small edit | `python verify.py --quick` |
| Full verification | `python verify.py` |
| Just run tests | `python verify.py --test-only` |
| Auto-fix lint issues | `python verify.py --fix` |

### 2. Interpret Results

| Check | What It Does | Common Failures |
|-------|--------------|-----------------|
| **Imports** | Core modules load | Syntax errors, missing deps |
| **Lint (ruff)** | Code style | F401 unused import, E501 line too long |
| **Types (mypy)** | Type mismatches | Missing return types, wrong args |
| **Flask Routes** | App initializes | Blueprint not registered |
| **Tests (pytest)** | Test suite | Assertion failures |

### 3. Summarize Failures

Provide actionable summaries with specific file:line references and fix commands.

### 4. Recommended Actions

| Failure | Action |
|---------|--------|
| Lint (fixable) | `python verify.py --fix` |
| Import errors | Check typos, missing deps, circular imports |
| Type errors | Add type hints or fix logic |
| Test failures | Read test file, understand expected behavior |
| Flask route errors | Check blueprint registration in `web/app.py` |

## Quick Reference

```bash
python verify.py           # Full verification
python verify.py --quick   # Skip type checking
python verify.py --fix     # Auto-fix lint issues
python verify.py --test-only  # Only run tests
```
