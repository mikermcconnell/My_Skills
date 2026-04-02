---
name: code-review-checklist
description: Systematic code review following security, performance, and maintainability best practices. Use when reviewing pull requests, code changes, or performing code audits.
---

# Code Review Checklist

When reviewing code, systematically check each category.

## 1. Security

- [ ] No hardcoded secrets, API keys, or credentials
- [ ] User input is validated and sanitized
- [ ] SQL/NoSQL queries use parameterized queries
- [ ] Authentication checks on protected routes
- [ ] Authorization checks (user can only access their data)
- [ ] No sensitive data in logs or error messages
- [ ] HTTPS for external API calls
- [ ] XSS prevention (escaped output, CSP headers)

## 2. Error Handling

- [ ] All async operations have try-catch or .catch()
- [ ] Errors provide user-friendly messages
- [ ] Errors are logged with sufficient context
- [ ] Failed operations don't leave state corrupted
- [ ] Network failures handled gracefully
- [ ] Loading states shown during async operations

## 3. Performance

- [ ] No unnecessary re-renders (React.memo, useMemo, useCallback where needed)
- [ ] Large lists use virtualization
- [ ] Images are optimized and lazy-loaded
- [ ] API calls are debounced/throttled where appropriate
- [ ] No N+1 query patterns
- [ ] Expensive computations are memoized
- [ ] Bundle size impact considered

## 4. Code Quality

- [ ] Functions do one thing (single responsibility)
- [ ] No magic numbers - use named constants
- [ ] No duplicate code - extract shared logic
- [ ] Variable/function names are descriptive
- [ ] Complex logic has explanatory comments
- [ ] No commented-out code
- [ ] Consistent formatting with project style

## 5. TypeScript

- [ ] No `any` types (use `unknown` if truly dynamic)
- [ ] Proper null checks (optional chaining, nullish coalescing)
- [ ] Interface/type definitions for data structures
- [ ] Generic types used appropriately
- [ ] Strict mode compliance

## 6. React Specific

- [ ] Hooks follow rules (no conditionals, proper deps arrays)
- [ ] Keys on list items are stable and unique
- [ ] Side effects in useEffect, not render
- [ ] Cleanup functions for subscriptions/timers
- [ ] Props destructured for clarity
- [ ] Component size reasonable (<200 lines)

## 7. Testing

- [ ] New functionality has tests
- [ ] Edge cases covered
- [ ] Tests are deterministic (no flaky tests)
- [ ] Mocks are appropriate and minimal

## 8. Accessibility

- [ ] Interactive elements are keyboard accessible
- [ ] Images have alt text
- [ ] Form inputs have labels
- [ ] Color contrast sufficient
- [ ] Focus states visible

## Review Response Format

```markdown
## Summary
Brief overview of what the code does and overall assessment.

## Strengths
- What's done well

## Issues
### Critical (must fix)
- Security/correctness issues

### Important (should fix)
- Performance/maintainability issues

### Minor (consider)
- Style/preference suggestions

## Questions
- Clarifications needed
```
