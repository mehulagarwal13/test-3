# Troubleshooting

**`ModuleNotFoundError` running the validation script**
The script only uses the Python standard library -- run it with `python tests/validate_repo.py` from the repository root, not from inside `tests/`.

**Git clone fails or times out**
Confirm you have network access to GitHub and, if using SSH, that your key is registered with your GitHub account.

**Push rejected**
Pull and rebase on the latest default branch, then push again.
