# Setup preflight: choose one working route

[Act home](../README.md) · [Troubleshooting](troubleshooting.md)

You need a terminal, Git, an editor, a GitHub account with repository access, and Python. Use macOS Terminal (zsh) or Windows **WSL Ubuntu** (bash) for the lesson command blocks. Windows PowerShell is a separate route below for Python only; POSIX folder commands in the lessons are intended for macOS/WSL.

## Before class

On macOS, install Git and Python from an instructor-approved source. On Windows, follow [Microsoft's WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install), then open Ubuntu; keep the project inside its Linux home folder, and open VS Code through its WSL extension if using that editor. WSL installation/restart is preflight work, not part of the 30-minute lesson exercise.

Run:

```bash
git --version
python3 --version
pwd
```

**Supported course baseline:** Python 3.12–3.14. This build is tested locally on 3.13 and 3.14; GitHub CI also checks 3.12. Use one instructor-approved version consistently. Below, `python3` must identify that version. If it does not, ask for the correct executable before creating the environment. Record actual version output, not the example version.

In GitHub, create a disposable personal repository and verify you can push before assessment day. HTTPS and SSH are both legitimate Git transports. For HTTPS use your configured credential manager or GitHub CLI authentication; GitHub account passwords are not Git push credentials. For SSH follow [GitHub's SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). Never paste tokens or private keys into submissions.

Set your commit identity once, using your approved name/email (GitHub's no-reply address is acceptable):

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR_APPROVED_EMAIL"
```

Replace placeholders; do not copy them literally. Authentication grants access; commit identity labels authorship. They solve different problems.

## Environment commands (Lesson 03 onward)

From the project root that contains `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip install -r requirements.txt
python -m pip check
```

The interpreter path should be inside this project's `.venv`; the final printed Boolean should be `True`. `pip check` should report no broken requirements. Installation downloads packages, so preflight network access matters. Use `python -m pip` to pair installation with the interpreter you selected.

In each new terminal, return to the project and activate its environment again. Alternatively use `.venv/bin/python` explicitly. Do not commit or copy `.venv`; recreate it from dependencies.

PowerShell Python equivalent (only if the instructor approves this route):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```

This uses the explicit interpreter and does not require an activation policy change. Select an installed approved version instead of `-3.12` if necessary. Use the editor for file creation if following PowerShell; do not paste the POSIX shell blocks unchanged.

## Ready means observed

- You know the current directory and chosen interpreter.
- You can clone and push a personal repository.
- You can open/edit a file in the same project the terminal uses.
- In Lesson 03 onward, dependencies install in the project environment.

The instructor publishes assessment transport, resource rules, accommodations, and deadlines in the actual test handout. This preflight does not set an institution-wide policy.
