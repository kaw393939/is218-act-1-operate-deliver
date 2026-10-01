# Disposable Git recovery lab

[Lesson 07](../lessons/07-recovery-ci.md)

Use a **new unused folder** `~/is218-labs/recovery-sandbox`. There is no remote. These commands are designed to change only this disposable repository. If it already exists, choose another name; do not erase earlier work.

## Required: unstage versus revert

```bash
cd ~/is218-labs
mkdir recovery-sandbox
cd recovery-sandbox
git init -b main
printf 'Baseline note\n' > note.txt
git add note.txt
git commit -m "Record baseline note"
printf 'Temporary addition\n' >> note.txt
git add note.txt
git diff --cached
git restore --staged note.txt
git diff
cat note.txt
```

Predict before the last two commands. The added line remains; it is unstaged. Record the difference between `git diff --cached` and `git diff` before/after unstaging.

Now commit that addition and reverse the **committed** change:

```bash
git add note.txt
git commit -m "Add temporary note"
git rev-parse HEAD
```

Copy the full SHA just printed. Replace `ADDITION_COMMIT_SHA` below with that value:

```bash
git revert --no-edit ADDITION_COMMIT_SHA
cat note.txt
git log --oneline -3
git status --short
```

Expect only `Baseline note` in the file, three commits, and clean status. The history retains the original addition and a new reversing commit. Explain why this is different from unstaging.

## Optional extension: resolve a deliberate conflict

Only after the required checkpoint, continue in this disposable repository:

```bash
git switch -c feature/wording
printf 'Feature wording\n' > note.txt
git add note.txt
git commit -m "Propose feature wording"
git switch main
printf 'Main wording\n' > note.txt
git add note.txt
git commit -m "Revise main wording"
git merge feature/wording
```

The merge should stop with a content conflict in `note.txt`. Inspect `git status` and the markers in the file. Decide the intended content; for this lab write `Main and feature agree on the final wording` as the single line. Remove all conflict markers, save, then:

```bash
git add note.txt
git commit -m "Resolve wording after comparing both changes"
cat note.txt
git status --short
```

Expect the chosen single line and clean status. Explain your content decision. If you need to cancel **while the conflict is unresolved**, `git merge --abort` returns to the pre-merge state. Do not use a hard reset to hide the exercise.

## Evidence

Working directory, unstage observation, reversal commit, and optional conflict reasoning. No remote push or GitHub PR is needed for this lab. Command typing alone does not establish understanding.
