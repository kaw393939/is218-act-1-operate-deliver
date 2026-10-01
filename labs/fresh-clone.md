# Fresh clone: another machine's question

[Lesson 07](../lessons/07-recovery-ci.md)

Can a reader recreate your project using the repository rather than your current untracked files or installed global packages?

Replace placeholders with your real student URL and submitted SHA. Choose an unused clone folder; this clone is separate from your working project.

```bash
cd ~/is218-labs
git clone https://github.com/YOUR_ACCOUNT/is218-act1-YOURNAME.git verification-clone
cd verification-clone
git checkout SUBMITTED_FULL_SHA
python3 -m venv .venv
source .venv/bin/activate
python -c "import sys; print(sys.executable); print(sys.version); print(sys.prefix != sys.base_prefix)"
python -m pip install -r requirements.txt
python -m pip check
python -m pytest -q
git rev-parse HEAD
git status --short
```

Checking out a SHA makes a detached HEAD suitable for inspecting an exact revision. Do not develop here unless you create a branch. If checkout fails, fetch the submitted branch or investigate whether the commit was pushed.

The environment path should be inside `verification-clone/.venv`, the Boolean `True`, and tests green. With the completed Lesson 06 reference, expect eight tests. Your exact number may include approved additional cases; identify the cases rather than treating count as proof. Git status should be clean because generated files are ignored.

Record the revision, interpreter version, dependency check, and test result. Then explain a remaining limitation: a fresh clone on your machine is not a test of every operating system or input.

Inspect the GitHub workflow run at the same SHA. Different revisions cannot support a claim about your final submission. If dependencies cannot download, state that reproduction is blocked at installation instead of claiming application failure or success.
