# Command reference: predict the target first

[Act home](../README.md)

These examples use macOS/WSL bash or zsh. Replace uppercase placeholders. Check `pwd`, repository identity, and branch before changes.

| Command | Purpose | Evidence to inspect |
| --- | --- | --- |
| `pwd` | Show current directory | Are you in the intended project? |
| `ls -a` | Include hidden names | `.git`, `.gitignore`, `.venv` are different things |
| `cd ..` | Go to parent directory | Run `pwd` afterward |
| `cat README.md` | Read text | It does not edit the file |
| `git status --short --branch` | Inspect work and current branch | `??` untracked; first status column staged; second unstaged |
| `git remote -v` | Inspect remote URLs | Is `origin` your student repository? |
| `git diff` | Inspect unstaged tracked changes | Untracked files do not appear here |
| `git diff --cached` | Inspect staged changes | These are the changes the next commit includes |
| `git add app/operations.py` | Stage one named path | Inspect staged diff before committing |
| `git restore --staged README.md` | Unstage, keep working edit | Does `git diff` still show the edit? |
| `git commit -m "Explain a focused change"` | Record staged state | A local commit has not yet been pushed |
| `git push -u origin FEATURE_BRANCH` | Publish branch | Inspect same commit on GitHub |
| `git switch -c FEATURE_BRANCH` | Create/switch local branch | Start from the intended base revision |
| `git log --oneline -5` | Recent history | Messages are claims; diffs show content |
| `git rev-parse HEAD` | Full current commit identity | Match submission and workflow run |
| `git pull --ff-only` | Advance without creating a merge | Stops when histories diverge; inspect instead of forcing |
| `python -m pytest -q` | Run tests with selected Python | Nonzero exit or failure output needs investigation |
| `python -m pip check` | Check dependency compatibility | Does not test arithmetic behavior |

## Recovery choices

Unstage with `git restore --staged PATH` when the file should remain edited. `git restore PATH` discards uncommitted working changes in that path; use only on intentional disposable edits. `git revert COMMIT_SHA` creates a new commit reversing a committed change; inspect its diff and rerun checks. Use the explicit SHA from your own history.

A merge conflict asks you to decide the intended content. Read both changes, edit out conflict markers, stage the resolved file, complete the merge, and verify. `git merge --abort` cancels an in-progress merge when you need to start again. This act does not need force pushes or hard resets.

A Git branch name is an identifier, not a folder. A pull request is a proposed integration plus discussion/review. Pushing the branch supplies the commits; merging is a separate action.
