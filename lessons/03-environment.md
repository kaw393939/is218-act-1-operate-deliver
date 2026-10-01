# Lesson 03: Select and reproduce a Python environment

[Act home](../README.md) · [Previous](./02-github.md) · [Next](./04-assertions.md)

**Week 2, meeting 1 · 80 minutes · 30 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/03-environment) · [AI boundaries](../docs/assistance.md)


## By the end you can

- Select and identify a project virtual environment.
- Install the declared test dependency through that interpreter.
- Prove generated environment files are ignored and not tracked.

**Opening retrieval (0–10):** Which program executes `python` in this terminal?

## The problem: “it works on my machine” hides dependencies

Two students type `pytest`. One has the package installed globally, the other does not. We want an environment another person can recreate and an interpreter whose identity we can prove.

## Read and predict (0–25)

An interpreter executes Python; a dependency is an external package; a virtual environment gives a project its own package environment. Activation selects a convenient command path in this shell. It does not permanently configure every future terminal. Read [the environment setup](../docs/setup.md).

Predict whether creating `requirements.txt` installs anything. Predict whether committing `.venv` is necessary for a peer to reproduce the project.

## Direct lab (25–55): select, install, inspect

Return to your **student** repository. In the editor create `.gitignore`:

```gitignore
.venv/
__pycache__/
.pytest_cache/
*.py[cod]
.DS_Store
```

Create `requirements.txt`:

```text
pytest==8.4.2
```

This act pins pytest for a consistent exercise environment. It is a test dependency; arithmetic will use Python itself.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip install -r requirements.txt
python -m pip check
python -m pytest --version
git check-ignore .venv/pyvenv.cfg
git status --short
git ls-files .venv
```

Expect an interpreter inside this project's `.venv`, `True`, pytest `8.4.2`, and an ignored `.venv/pyvenv.cfg`. The last command should print nothing: the environment is not tracked. We have not created tests yet, so do not mistake “no tests collected” for an arithmetic check.

Stage only the authored configuration and README setup instructions. Inspect the staged diff, commit, and push. Do not commit generated packages.

**Independent variation:** open a new terminal, return to the project, inspect Python selection, activate the same environment, and inspect again. Explain the observed difference, including if your shell already used the same interpreter.

## Critique (55–75)

Compare evidence with a partner. Outside direct practice, ask AI to diagnose a hypothetical missing-pytest error from interpreter and path information. Decide whether its proposed fix targets the intended environment.

## Exit evidence (75–80)

Record interpreter path/version, `pip check`, pytest version, and the tracked-file/ignore checks. Start [Week 2](../assignments/week-2.md).

## Stuck or ahead?

Use `python -m pip`, not a guess about which `pip` belongs to which interpreter. If `.venv` was already committed, an ignore rule alone cannot untrack it; consult the specific recovery in [troubleshooting](../docs/troubleshooting.md). Faster learners explain why copying an environment to another path can break it.

**Instructor checkpoint:** verify the selected interpreter and untracked environment. A hosted CI run cannot replace this local check.
