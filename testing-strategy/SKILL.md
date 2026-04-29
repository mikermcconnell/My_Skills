---
name: testing-strategy
description: Test writing best practices with arrange-act-assert pattern, mocking strategies, and coverage priorities. Use when writing unit tests, integration tests, or discussing testing approaches.
---

# Testing Strategy

Use this skill to choose what to test, structure tests clearly, and keep mocking practical instead of overcomplicated.

## Use these references

Read only what you need:
- `references/test-priorities-and-patterns.md` for coverage priorities, AAA examples, and naming guidance
- `references/mocking-and-helpers.md` for mocking strategies, helpers, and anti-patterns

## Workflow

1. Identify the test target: pure function, business logic, component behavior, hook, or integration flow.
2. Start with the highest-value behavior first.
3. Use Arrange-Act-Assert structure unless the framework strongly prefers something else.
4. Mock only what the test genuinely depends on.
5. Prefer readable tests that explain expected behavior over clever abstractions.

## Core rules

- Test behavior, not implementation trivia.
- Prioritize logic and user-visible behavior over exhaustive coverage theatre.
- Keep each test focused on one meaningful outcome.
- Use factories and helpers to reduce repetition, but don't hide intent.
- Name tests so failures explain what broke.

## Gotchas

- Don't over-mock and then pretend the test proves real behavior.
- Don't snapshot everything just because it's easy.
- Don't test framework internals or third-party library behavior.
- Don't pack multiple assertions about unrelated outcomes into one test.
- Don't let helpers make the test harder to read than the test body itself.
