---
name: typescript-strict
description: TypeScript strict mode patterns including proper typing, avoiding any, branded types, and null safety. Use when writing TypeScript code, fixing type errors, or reviewing type definitions.
---

# TypeScript Strict Mode Patterns

Use this skill to keep TypeScript code precise, readable, and safe under strict settings.

## Use these references

Read only what you need:
- `references/strict-typing-patterns.md` for core rules, avoiding `any`, branded types, null safety, unions, and utility types
- `references/react-and-function-typing.md` for function signatures, component props, and common mistakes

## Workflow

1. Identify the type problem: dynamic data, nullability, API shape, unions, or props.
2. Choose the narrowest type that still matches reality.
3. Prefer explicit modeling over escaping with `any`.
4. Add small guards, helper types, or branded types where they improve safety.
5. Keep the final types readable enough that the next person can maintain them.

## Core rules

- Avoid `any`; use `unknown` when the value is truly dynamic.
- Handle `null` and `undefined` explicitly.
- Use branded types when different IDs or tokens should never be mixed.
- Prefer discriminated unions over loosely related optional fields.
- Keep public function signatures clear.

## Gotchas

- Don't use `as` casts to silence real uncertainty.
- Don't create ultra-clever types that nobody can debug later.
- Don't use one giant interface when a union better matches reality.
- Don't treat optional and nullable as the same thing.
- Don't let convenience undo the value of strict mode.
