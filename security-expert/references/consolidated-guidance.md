# Consolidated security hardening guidance

Read this when work crosses an authentication, authorization, data, file, network, or external-service boundary.

- Map trusted and untrusted inputs and the assets each path can reach.
- Validate at the boundary and authorize every protected action server-side.
- Use least privilege for identities, tokens, rules, and service accounts.
- Keep secrets out of source, client bundles, errors, and logs.
- Consider injection, unsafe file paths, request forgery, dependency risk, abuse, and data leakage.
- Add negative tests for unauthorized and malformed requests, then document residual risk.
