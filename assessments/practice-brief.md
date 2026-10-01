# Independent practice: build–test–deliver

[Preparation specification](test-1.md)

Use a new personal repository, not a textbook branch. Rehearse without AI or peer repair. Use the course command reference. Aim for 65 minutes execution plus a deliberate final handoff; repeat after diagnosing gaps.

## Brief

Build `app/operations.py` with `add(a, b)` returning `a + b` and `subtract(a, b)` returning `a - b` for ordinary finite integer/float operands. Include `app/__init__.py`. In `tests/test_operations.py` write six explicit AAA tests:

- Addition with positive operands.
- Addition with negative operands.
- Addition with one zero operand.
- Subtraction with positive operands.
- Subtraction with negative operands.
- Subtraction yielding a negative result.

Choose your own integer examples; independently calculate expected values. Create `.gitignore`, `requirements.txt` pinning `pytest==8.4.2`, and a README with reproducible install/test commands. Copy the supplied student test workflow from Lesson 07. Do not add a UI or classes.

Create two issues: one for environment/README configuration, one for arithmetic and tests. Complete each on a focused branch, commit with the related issue number, and integrate into your own `main`. Inspect before staging/merging. Verify local tests and hosted workflow at the final SHA.

## Handoff

Submit to your own practice log (not the instructor textbook): repository URL, full final SHA, matching run URL, actual interpreter/environment evidence, and a paragraph explaining one test expectation and one limit of CI. Evaluate with the public preparation rubric. If CI is inaccessible, record the block and complete local verification; do not claim a hosted pass.

This practice uses the same tool workflow as the proposed official test. The official task may vary repository/signature details, operands/case labels, and a small behavior detail. It will announce every requirement and its criteria. Memorizing this brief is not preparation for reasoning about those variations.
