# Consolidated simplification guidance

Read this when working code is unnecessarily complex.

- Write down behavior that must not change before restructuring.
- Remove dead indirection, duplicated branches, and abstractions with only one real use.
- Prefer clear data flow and ordinary language over clever patterns.
- Make one structural change at a time and run the narrowest meaningful test after each.
- Stop when additional cleanup no longer reduces maintenance cost.
