# How to use this book

[Act home](../README.md)

There are two different workspaces. The **textbook clone** lets you inspect examples. Your **student repository** records what you personally build, test, and submit. Name the latter `is218-act1-YOURNAME` so you can tell them apart.

Every lesson follows predict → operate → observe → explain. Before running a command, say which directory or revision it acts on. Afterward, check the result instead of relying on the absence of an error.

## Reading and branch workflow

Read the handout on GitHub's `main`. If you want the matching complete example locally:

```bash
git clone https://github.com/kaw393939/is218-act-1-operate-deliver.git
cd is218-act-1-operate-deliver
git status --short
git switch --track origin/lesson/04-assertions
```

The first switch creates a local tracking branch; later use `git switch lesson/04-assertions`. Check status before switching; preserve edits by committing on your own branch. Avoid editing the textbook during an assignment. References 01–02 contain file/Git examples; 03 adds the environment; 04 adds arithmetic and tests; 05–06 model focused change/review artifacts; 07 adds CI; 08 retains the practice state and assessment preparation, not an exam answer.

## What counts as learning

A command transcript alone is insufficient. Explain why that command was appropriate and what its output supports. A green test run supports the cases executed at that revision. It does not prove every input, the quality of a review, or whether you used a local virtual environment.

Use [the evidence template](../templates/evidence.md). Keep observations concise. Do not invent output, peer participation, or AI disclosure. Small honest observations are more useful than polished unsupported claims.

## Pacing and help

Meetings are 80 minutes. Direct blocks are personally operated work with AI generation paused. Use the printed commands, instructor help, and permitted peer checks. Outside these blocks, use AI to explain or critique a bounded issue and verify its claims. See [the assistance policy](assistance.md).

If setup fails, stop at the first unexpected output and use [troubleshooting](troubleshooting.md). An instructor-approved temporary machine can support practice; mark uncompleted local setup accurately. Extension activities are optional and carry no hidden assessment requirement.
