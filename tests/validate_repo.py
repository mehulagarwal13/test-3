"""Lightweight onboarding-repository validation for test-3.

Usage example (also the closest thing this repository has to a "run"
command right now):

    python tests/validate_repo.py

Confirms the repository's core documentation exists and is non-empty --
intentionally simple so a brand-new contributor can read the whole script
in under a minute.
"""
from __future__ import annotations

import pathlib
import sys

REQUIRED_FILES = ["README.md"]


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    failures = []

    for name in REQUIRED_FILES:
        path = repo_root / name
        if not path.exists():
            failures.append(f"missing required file: {name}")
        elif path.stat().st_size == 0:
            failures.append(f"required file is empty: {name}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: onboarding validation succeeded -- README.md is present and non-empty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
