# Mocking and Helpers

## Mocking guidance

- Mock external services and unstable boundaries.
- Mock the smallest useful surface area.
- Use realistic fake responses.
- Prefer integration-style tests over deep mocking when practical.

## Common patterns

Useful candidates for mocking:
- API clients
- Firebase or database access
- browser APIs not available in the test runtime
- clock, randomness, network, or file system boundaries

## Helpers and factories

Helpers are useful when they:
- remove repetitive setup
- keep defaults sensible
- make test intent easier to read

Helpers are harmful when they:
- hide critical context
- create giant object graphs nobody understands
- require readers to jump through multiple files to understand a simple test
