<!-- SafeSwipe/docs/workflow.md -->

# SafeSwipe — Team Workflow

## Purpose
This document defines how we work day to day: branching, commits, and reviews. Everyone should follow this the same way, every time.

## Branching
- `main` is always stable and deployable-ready. We never commit to it directly (except this repo's very first setup commit).
- Every change happens on its own branch, named like:
  - `docs/<short-topic>` for documentation
  - `feat/<short-topic>` for new features (once we reach code)
  - `fix/<short-topic>` for bug fixes

## Commits
- Small, focused commits. One logical change per commit.
- Commit message format: `<type>: <short description>` — e.g. `docs: add workflow guide`
- Types we use: `docs`, `feat`, `fix`, `chore`

## Pull Requests
- Every branch gets merged into `main` through a Pull Request — never a direct push.
- At least one other team member should look at the PR before merging, even if it's small.
- Keep PRs small and reviewable — this is more important than moving fast.

## Status
This is a living document — update it if we agree to change how we work.