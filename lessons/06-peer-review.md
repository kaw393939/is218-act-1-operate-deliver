# Lesson 06: Collaborate through a pull request

[Act home](../README.md) · [Previous](./05-focused-commits.md) · [Next](./07-recovery-ci.md)

**Week 3, meeting 2 · 80 minutes · 25 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/06-peer-review) · [AI boundaries](../docs/assistance.md)


## By the end you can

- Author and review a bounded PR in rotated roles.
- Connect a review comment to a test claim or documentation gap.
- Respond to feedback and verify the integrated revision.

**Opening retrieval (0–10):** What could a green test run leave unreviewed?

## The problem: “looks good” is not a review

Your partner's tests are green. You still need to inspect whether they check the intended behavior. A pull request connects authorship, discussion, revision, and integration.

## Read and predict (0–25)

A push publishes a branch; a pull request proposes its integration. A reviewer needs a specific claim and supporting evidence. Use your Lesson 05 issue/branch for the first review round; the second round gives your partner an authored change and you a review.

Pair on **one student's repository** for this weekly assignment. The owner grants the partner collaborator access through GitHub settings, following instructor visibility rules. Both clone that repository separately. Preserve individual Week 2 repositories. If access fails, contact the instructor for an approved fork-PR route; do not substitute a fictional peer review.

## Direct lab (25–50): review and respond

1. Author A opens a PR from `feature/mixed-sign-addition` to `main`. State the issue, behavior, actual test command/result, and limits using [the PR template](../templates/pull-request.md).
2. Reviewer B reads the diff, checks the expected value independently, and checks out the feature branch in their own clone to run tests. They leave a concrete review comment. Example: “The mixed-sign case is correct; document which existing test covers zero so a reader can find that evidence.” Identify a real gap rather than demanding an unnecessary feature.
3. Author A addresses the comment in a focused follow-up commit, reruns tests, and replies with the evidence. Reviewer B inspects the follow-up before approving. The author merges using GitHub after review and passing checks available at this stage.
4. In each local clone, switch to `main`, run `git pull --ff-only`, rerun tests, and record the integrated SHA.

For Reviewer B's fresh clone, inspect the remote and obtain the first branch before reviewing:

```bash
git remote -v
git fetch origin
git switch --track origin/feature/mixed-sign-addition
python -m pytest -q
```

If that local tracking branch already exists, switch to it by name and inspect whether it matches the pushed revision. A reviewer should not repair the author's branch silently; request a follow-up through the PR.

Then rotate. Author B opens an issue and branch adding an eighth explicit test `subtract(5, 0) == 5`; Reviewer A performs the same review/response/integration process. Complete the second round during the integration block or weekly assignment time if needed.

Branch setup for round two, from clean updated `main`:

```bash
git switch -c feature/subtraction-zero
python -m pytest -q
git status --short
```

Add/edit before the test run as appropriate. Stage only intended files, commit, push this branch, and create the PR through GitHub. After integration the worked checkpoint has eight passing tests.

## Critique and integration (50–75)

Finish the rotated round. Compare “LGTM” with a review that states a case, an independently checked expected value, and a remaining limitation. Outside direct practice, AI may critique a draft review, but the reviewer owns the actual inspection and final statement.

## Exit evidence (75–80)

Each student supplies one authored PR, one substantive review, one response to feedback, and a post-merge SHA/test result. Complete [Week 3](../assignments/week-3.md).

## Stuck or ahead?

A local branch may lag behind the merged remote. Inspect branch/remote before testing. A self-review can be useful practice but does not meet the pair requirement; arrange an instructor-approved alternative if a partner is absent. Faster pairs explain squash versus merge history without changing shared history unnecessarily.

**Instructor checkpoint:** identify each student's authored and reviewed contribution; do not grade by commit count. No student needs to open a PR against the textbook repository.
