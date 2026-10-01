# Instructor guide: teach ownership of evidence

[Act home](../README.md)

## Learning design

Begin each meeting with a concrete failure of confidence: wrong directory, unpublished commit, wrong interpreter, misleading assertion, unrelated staged file, shallow review, or unidentified CI failure. Ask a prediction before demonstration. The direct task is deliberately small so students personally operate the tool; critique blocks connect observations to vocabulary and AI management.

The cumulative reference program is not a large application. Stop at two functions and eight explicit tests. Larger architecture would obscure this act's tool outcomes. Each lesson handout includes checkpoints, specific expected observations, recovery routes, and an optional extension. Assess explanations connected to artifacts, not terminology recall alone.

## Before teaching

- Publish actual deadlines, LMS channel, repository visibility, accommodations, and semester grading in the authoritative course syllabus/announcements.
- Check macOS/WSL setup and authentication **before** timed exercises. The Windows route is documented but has not been run on a Windows machine in this build; arrange a Windows learner pilot.
- Run the author verification command below and inspect hosted CI. Dependency/network/auth delays require pacing judgment; budgets are not a tested guarantee.
- Pilot a full independent setup journey, a rotated pair review, and a timed practice attempt. Record completion time and where learners hesitate.
- Use official Test 1 materials separately. Do not add solutions or hidden variants to any public branch.

## Meeting pacing

Lessons 01–04 allocate 30 direct minutes each; 05–06 allocate 25; 07 allocates 21; 08 allocates 65. Total 256/640 = 40%. All normal meetings: 0–10 retrieval, 10–25 demonstration, direct task, critique/integration to minute 75, then five-minute exit. Test 1 uses its separately listed 5/65/10 agenda.

Classroom pace may require finishing the second PR/fresh-clone download within the weekly assignment. Do not label watching or AI-generated commands as completed direct practice. Optional conflicts/extra numeric tests are not hidden rubric criteria.

## Formative feedback

Ask “Which state contains the edit?” rather than “Did you do Git?” Ask “What independently supports this expected result?” rather than “Is pytest green?” Inspect individual explanations; remediate a specific gap before accumulating complexity.

Week 3 pairs earn a shared integrated-behavior evaluation plus individual authorship/review evidence. Rotate both roles. A missing partner is a coordination issue requiring an explicit alternative. Do not infer effort from code volume or commit count.

## Verify this textbook

From `main`, install requirements in a fresh environment and run:

```bash
python tools/verify_course.py --full
```

The verifier checks local Markdown paths/anchors, branch presence, cumulative file expectations, clean archived snapshots, arithmetic tests and a deliberate defect, and the disposable recovery sequence. GitHub runs that verification on Python 3.12–3.14. Ordinary learner repositories use the smaller supplied student-test workflow.

Source revisions and author-versus-learner verification boundaries are in [sources](sources.md). This authoring pass validates reproducible mechanics; learner efficacy and timing still require a pilot.
