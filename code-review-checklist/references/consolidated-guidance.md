# Consolidated review guidance

Read this for high-risk or broad reviews that need more than the core checklist.

- Review correctness and regression risk before style.
- Trace changed inputs through state, side effects, persistence, and user-visible outputs.
- Check trust boundaries, failure handling, concurrency, performance, and maintainability.
- Challenge hidden assumptions with one plausible failure scenario.
- Distinguish blocking findings from optional improvements.
- Require evidence for resolved findings rather than accepting intent.
