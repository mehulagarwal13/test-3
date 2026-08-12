# Contributing to test-3

Thank you for your interest in contributing to `test-3`. This guide covers how to report issues, branch and commit conventions, the pull request checklist, local testing, and the review process.

## Onboarding Checklist

New contributors should, in order:

- [ ] Read [`docs/prerequisites.md`](docs/prerequisites.md)
- [ ] Follow [`docs/setup.md`](docs/setup.md)
- [ ] Run `python tests/validate_repo.py` successfully
- [ ] Read [`docs/usage-example.md`](docs/usage-example.md) for a worked example before making a first change

## Reporting Issues

Search existing issues first. Include a clear title, expected vs. actual behavior, and reproduction steps where applicable.

## Branch Naming

- `docs/<topic>` for documentation-only changes
- `test/<topic>` for test-only changes
- `fix/<topic>` for bug fixes
- `feature/<topic>` for new functionality

## Commit Messages

```text
<type>: <short, present-tense summary>
```

## Pull Request Checklist

- [ ] The PR description explains *why*, not just *what*
- [ ] `python tests/validate_repo.py` passes locally
- [ ] Any related issue is linked

## Review Process

Every pull request should have at least one review before merging.
