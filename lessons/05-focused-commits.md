# Lesson 05: Make a focused issue and commit

[Act home](../README.md) · [Previous](./04-assertions.md) · [Next](./06-peer-review.md)

**Week 3, meeting 1 · 80 minutes · 25 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/05-focused-commits) · [AI boundaries](../docs/assistance.md)


## By the end you can

- State one issue with observable acceptance checks.
- Selectively stage and inspect a focused change.
- Explain which edit belongs to the commit and which remains outside it.

**Opening retrieval (0–10):** Can a commit message prove its actual contents?

## The problem: a commit silently includes unrelated work

You improved a test and edited learning notes. Should both be part of the same proposed change? A focused commit lets a reviewer inspect a claim without unrelated noise.

## Read and predict (0–25)

Git has current files, staged content, and recorded commits. An issue states a problem and acceptance checks; it is not just a task label. Predict which diff will include a staged test edit but exclude an unstaged README edit.

## Direct lab (25–50): one issue, one inspectable change

In your student GitHub repository, open an issue titled “Verify addition with mixed signs.” Acceptance: a new explicit test checks one positive and one negative operand, calculates an independent result, and leaves the six existing tests green. Record the issue number.

From a clean student working tree:

```bash
git switch main
git pull --ff-only
git switch -c feature/mixed-sign-addition
```

Create a seventh test such as `add(8, -3) == 5`, following AAA. Separately append a personal reflection to README. Save both, then inspect:

```bash
git status --short
git diff
git add tests/test_operations.py
git diff --cached
git diff
python -m pytest -q
```

The staged diff should contain the test; the unstaged diff should contain the README edit. Commit the test only, referencing your real issue number, for example `git commit -m "Test mixed-sign addition; refs #1"`. Then inspect `git show --stat HEAD`. Expect seven passing tests.

After proving selective staging, commit the README reflection separately. Push the feature branch with `git push -u origin feature/mixed-sign-addition`. Keep the branch available for Lesson 06; do not merge it yet.

**Independent variation:** stage README, then use `git restore --staged README.md` **before** committing it. Show that the edit remains in the working file. This reverses staging, not authorship.

## Critique (50–75)

Compare an issue acceptance check with the new test. Outside direct practice, ask AI whether “improve tests” is an adequate issue description. Rewrite it into an observable behavior. The worked snapshot adds the seventh test and a sample scope note; it does not pretend a local commit proves a GitHub issue existed.

## Exit evidence (75–80)

Issue URL, focused test commit SHA, staged/unstaged distinction, and the passing run. This feeds [Week 3](../assignments/week-3.md).

## Stuck or ahead?

`git diff` excludes untracked files and staged changes. Use status and staged diff together. If unrelated files are already staged, unstage the specific path and inspect again. Faster learners explain why `refs #N` records a relationship whereas `Closes #N` in an integrated PR can close the issue.

**Instructor checkpoint:** ask “What exactly is in this commit?” Accept evidence from the diff, not merely the message.
