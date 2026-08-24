---
name: git-workflow-and-versioning
description: Safely inspect, organize, branch, commit, merge, and review Git changes without disturbing unrelated work. Use when making code changes, handling a dirty worktree, preparing commits, resolving conflicts, using worktrees, or planning version-control steps.
---

# Git workflow and versioning

## Safety first

- Inspect status, branch, and diff before editing or committing.
- Treat existing modified and untracked files as user work unless proven otherwise.
- Do not discard, overwrite, reset, clean, stash, amend, rebase, or force-push without explicit permission.
- Keep unrelated changes out of the task's commit.

## Workflow

1. Read repository instructions and inspect the worktree.
2. Choose the smallest safe isolation method: current branch, new branch, or worktree.
3. Make focused changes and verify them before staging.
4. Review the staged diff for secrets, generated noise, and accidental files.
5. Use an atomic commit with a message that explains intent.
6. Report the branch, commit, verification, and any remaining user changes.

## Parallel work

Use separate worktrees when concurrent tasks could touch the same repository. Never assume another agent's uncommitted files are safe to move or delete.

## Commit messages

Use `commit-conventions` when a commit is requested. Do not create a commit merely because code changed unless the user or repository workflow calls for it.

## Deeper reference

Read [references/legacy-skill-2026-07.md](references/legacy-skill-2026-07.md) only for detailed branching, worktree, or history-investigation examples.
