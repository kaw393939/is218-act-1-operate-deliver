# Lesson 07: Recover and verify in a fresh environment

[Act home](../README.md) · [Previous](./06-peer-review.md) · [Next](./08-test-1-preparation.md)

**Week 4, meeting 1 · 80 minutes · 21 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/07-recovery-ci) · [AI boundaries](../docs/assistance.md)


## The problem: failure has more than one layer

A workflow is red. Did dependency installation fail, did the program import incorrectly, or did an assertion expose wrong behavior? Recovery begins by identifying the state and failing stage.

## Read and predict (0–25)

Unstaging preserves an edit; restoring a working file can discard it; reverting creates a new inverse commit. A merge conflict requires a content decision. CI runs checks in another environment at a recorded commit. It cannot prove which interpreter you used locally.

Before class, read [the disposable recovery lab](../labs/recovery.md). Its conflict exercise is an optional extension after the required short recovery; setup for conflicts can exceed the 21-minute block.

## Direct lab (25–46): recover and reproduce

1. Use the disposable recovery lab's **required unstage/revert exercise**. Explain the distinct outcomes and record evidence. Do not experiment on a peer's project.
2. Return to your student repository. Copy the following **test workflow**, creating `.github/workflows/tests.yml` in the editor:

```yaml
name: Student tests
on: [push, pull_request, workflow_dispatch]
permissions:
  contents: read
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest -q
```

Commit/push and inspect the Actions run. This uses a provided workflow, not an exercise in memorizing YAML. Its executed tests are your repository's tests.

3. Make a **new clone in a different folder**, not a copied `.venv`. Use your real repository URL, create a new environment, install dependencies, run tests, and compare `git rev-parse HEAD` with the submitted revision. See [the fresh-clone checklist](../labs/fresh-clone.md).

A dependency download or push may continue after the direct block; record delays honestly and finish during the integration block/Week 4 assignment time. Expect eight passing tests after the pair checkpoint.

## Diagnose and integrate (46–75)

In a temporary feature branch, deliberately change a test expectation to an incorrect value. Push, inspect the failing assertion step, then correct it and confirm green. Do not merge the deliberate defect. Record the two run URLs/SHAs. The broken test is a demonstration of the pipeline, not a behavior fix. Optional: complete the merge-conflict extension with a peer and explain the chosen final text.

## Exit evidence (75–80)

Recovery explanation, fresh-clone interpreter/revision, and a workflow run tied to the corrected SHA. Submit [Week 4](../assignments/week-4.md). Explain one fact CI did not establish.

## Stuck or ahead?

A dependency or authentication failure can prevent tests from starting. Do not alter expected arithmetic values to fix those stages. Hosted Actions availability depends on repository/account settings; report an access block and perform local reproduction while the instructor resolves it. Faster learners compare local versus hosted interpreter versions.

**Instructor checkpoint:** use a failing run's actual log, not its badge alone. The textbook has separate course-material checks; the student's arithmetic workflow does not grade peer-review quality or local setup.
