# Sources, adaptation, and verification

[Act home](../README.md)

This book synthesizes earlier IS218 teaching material into eight bounded meetings. It uses newly authored prose and small original worked exercises rather than copying entire source assignments with conflicting environments or policies.

## Source revisions inspected

| Source | Inspected revision | Contribution |
| --- | --- | --- |
| [IS218_Example_Fall2026](https://github.com/kaw393939/IS218_Example_Fall2026/tree/82b018af02cea487838522807376d34d669be5c1) | `82b018af02cea487838522807376d34d669be5c1` | Terminal setup, issues, focused commits, pair PRs, recovery, CI |
| [is218_handsOn1_example](https://github.com/kaw393939/is218_handsOn1_example/tree/9d00fe46f1e9fd546ef2c41b1b6a0f21a442e591) | `9d00fe46f1e9fd546ef2c41b1b6a0f21a442e591` | Small addition/subtraction and explicit AAA test scope |
| [is218_test1_official](https://github.com/kaw393939/is218_test1_official/tree/e2f0d77a081660258a09767275ab43f7e0bf5559) | `e2f0d77a081660258a09767275ab43f7e0bf5559` | Independent assessment, evidence boundaries, no-AI test conditions |

The new practice brief is not a republication of the official prompt or an answer key. Its public preparation conditions do not silently change the source's official rules.

## Primary tool references

- [Python venv documentation](https://docs.python.org/3/library/venv.html): isolated project environments and explicit interpreter invocation.
- [pytest invocation](https://docs.pytest.org/en/stable/how-to/usage.html): running through the chosen interpreter.
- [Git documentation](https://git-scm.com/docs): inspect individual command semantics.
- [GitHub Python CI guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python): hosted Python setup and test execution.
- [Microsoft WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install): approved Windows terminal route.

## Verification scope

Author validation checks all eight branch snapshots from archived revisions, local links/anchors, Python snippets, expected test counts, a defect detected by the tests, and Git recovery outcomes. Hosted CI verifies Python 3.12, 3.13, and 3.14. Test output is evidence of those checks only; source repositories have been inspected, not exhaustively retested by this book build.

Not yet validated: Windows/WSL on a Windows machine, real student completion time, institutional calendar/policy fit, or effectiveness with a particular cohort. Instructor timing and learner pilots are required before calling those established.
