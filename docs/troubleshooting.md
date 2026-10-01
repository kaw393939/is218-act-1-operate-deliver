# Diagnose the first unexpected result

[Act home](../README.md) · [Setup](setup.md)

| Observation | First check | Recovery |
| --- | --- | --- |
| File not found | `pwd`, `ls -a` | Navigate to the intended root; do not create duplicate folders to hide it |
| `python3` not found/wrong version | Approved installation and executable | Complete preflight; ask for the correct executable |
| No module named pytest | `python -c "import sys; print(sys.executable)"` | Activate intended `.venv`; install through `python -m pip` |
| No module named app | Current directory and package files | Run `python -m pytest` from root; ensure `app/__init__.py` exists |
| Git author identity unknown | `git config user.name`, `git config user.email` | Set approved identity; this is separate from authentication |
| Permission denied pushing | `git remote -v` and auth route | Check ownership/access and configured credentials; do not expose tokens |
| Nothing to commit | Status, saved editor buffer, staged diff | Save correct file and stage intended paths |
| `.venv` tracked | `git ls-files .venv` | Add ignore rule; `git rm -r --cached .venv` stops tracking but keeps local files; inspect before commit |
| Merge conflict | `git status`, conflicted file | Resolve meaning, remove markers, stage and commit; or `git merge --abort` |
| CI red | Run commit SHA, job, first failing step | Distinguish dependency install, import, assertion, and course-material failures |
| Push rejected after peer merge | Inspect history and remote | Fetch/reconcile with help; do not force-push shared history |

Keep the smallest useful excerpt of the error, the command, current directory, and interpreter/revision. Ask for a diagnosis with those facts. Do not paste credential files. State which repair you tried and its observed result.

If an optional extension fails, return to the required checkpoint before adding more moving parts. Timed assessment access problems must be reported to the instructor; they are not permission to use AI or peer repair.
