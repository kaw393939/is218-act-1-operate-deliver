# Lesson 02: Connect a local project to GitHub

[Act home](../README.md) · [Previous](./01-terminal.md) · [Next](./03-environment.md)

**Week 1, meeting 2 · 80 minutes · 30 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/02-github) · [AI boundaries](../docs/assistance.md)


## By the end you can

- Inspect the student repository remote before publishing.
- Commit a focused README change and match local/remote revision identity.
- Explain saved, staged, committed, and pushed state with evidence.

**Opening retrieval (0–10):** Which of yesterday’s file changes were already commits?

## The problem: saved, committed, and published are different

You saved a README. Your partner cannot see it on GitHub. Which state is missing? A local file, a local commit, and a remote commit are distinct evidence.

## Read and predict (0–25)

A repository stores revision history. A commit records staged state locally. A remote names a place to exchange commits. `origin` is a conventional name, not a guarantee that it points to your account. Read [setup authentication](../docs/setup.md) before this meeting.

Predict: after editing a file but before committing, can GitHub display your new content? After committing but before pushing?

## Direct lab (25–55): your own repository

On GitHub, create **your own** `is218-act1-YOURNAME` repository, initialize it with a README, and choose visibility according to the instructor's submission rules. Replace `YOUR_ACCOUNT` and the repository name below with actual values. Copy the HTTPS clone URL from your repository; use the SSH URL instead if that is your configured approved route.

```bash
cd ~/is218-labs
git clone https://github.com/YOUR_ACCOUNT/is218-act1-YOURNAME.git
cd is218-act1-YOURNAME
pwd
git status --short --branch
git remote -v
```

`origin` must identify your student repository. Open README in the editor; add your learning goal and save. Then:

```bash
git diff
git add README.md
git diff --cached
git commit -m "Document my Act 1 learning goal"
git log --oneline -1
git push origin main
git rev-parse HEAD
```

Inspect GitHub's README and latest commit. The full local SHA must match the published revision. If your initialized default branch has another name, inspect it and use that actual name; this course examples assume `main`.

**Independent variation:** add a short section explaining the difference between commit and push. Commit/push it, then show your partner the revision containing that explanation.

## Critique (55–75)

Trace `edit → stage → commit → push → inspect GitHub`. A push moves commits, not every file currently on disk. Ask a partner to identify which state holds an unstaged edit. Outside direct practice, ask AI whether a commit guarantees correctness; use a concrete counterexample to critique its answer.

## Exit evidence (75–80)

Repository URL, full submitted SHA, remote identity, and an explanation of what existed locally before the push. Submit once for [Week 1](../assignments/week-1.md).

## Stuck or ahead?

An author identity error concerns commit labels; a permission error concerns access. Diagnose separately using [troubleshooting](../docs/troubleshooting.md). Do not push to the instructor textbook. Faster learners inspect `git show --stat HEAD` and explain which files that commit contains.

**Instructor checkpoint:** compare local SHA with GitHub, and ask “Would this push publish an uncommitted file?”
