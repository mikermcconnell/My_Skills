# Consolidated frontend performance guidance

Read this when the bottleneck is browser rendering, loading, or interaction responsiveness.

- Establish a baseline and a user-visible target before changing code.
- Separate network, CPU, rendering, memory, and third-party costs.
- Reduce unnecessary work before adding caching or complexity.
- Test representative data and slower devices, not only an empty local environment.
- Re-measure after each change and retain only improvements that materially affect users.
