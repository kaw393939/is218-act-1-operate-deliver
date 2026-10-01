"""Author checks for readings and cumulative branch examples; not a student grader."""
from pathlib import Path
import argparse
import ast
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def run(args, cwd=ROOT, expected=0):
    result = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode != expected:
        raise AssertionError(f'{args}: expected {expected}, got {result.returncode}\n{result.stdout}')
    return result.stdout


def anchor(title):
    title = title.lower().strip()
    title = ''.join(c for c in title if c.isalnum() or c in ' -_')
    return title.replace(' ', '-')


def check_docs(folder):
    count = 0
    for path in folder.rglob('*.md'):
        if any(part.startswith('.') for part in path.relative_to(folder).parts):
            continue
        body = path.read_text()
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if re.match(r'[a-z]+:', target):
                continue
            target = unquote(target)
            file, _, fragment = target.partition('#')
            dest = (path.parent / file).resolve() if file else path
            assert dest.is_relative_to(folder.resolve()), (path, target)
            assert dest.exists(), (path, target)
            if fragment:
                headings = re.findall(r'^#+\s+(.+)$', dest.read_text(), re.M)
                assert fragment in [anchor(h) for h in headings], (path, target)
        for snippet in re.findall(r'```python\n(.*?)```', body, re.S):
            ast.parse(snippet)
        count += 1
    return count


def recovery_check():
    with tempfile.TemporaryDirectory(prefix='act1-recovery-') as tmp:
        folder = Path(tmp)
        run(['git', 'init', '-b', 'main'], folder)
        run(['git', 'config', 'user.name', 'Verification'], folder)
        run(['git', 'config', 'user.email', 'verification@example.invalid'], folder)
        note = folder / 'note.txt'
        note.write_text('Baseline note\n')
        run(['git', 'add', 'note.txt'], folder)
        run(['git', 'commit', '-m', 'Baseline'], folder)
        note.write_text('Baseline note\nTemporary addition\n')
        run(['git', 'add', 'note.txt'], folder)
        assert 'Temporary addition' in run(['git', 'diff', '--cached'], folder)
        run(['git', 'restore', '--staged', 'note.txt'], folder)
        assert not run(['git', 'diff', '--cached'], folder)
        assert 'Temporary addition' in run(['git', 'diff'], folder)
        run(['git', 'add', 'note.txt'], folder)
        run(['git', 'commit', '-m', 'Addition'], folder)
        sha = run(['git', 'rev-parse', 'HEAD'], folder).strip()
        run(['git', 'revert', '--no-edit', sha], folder)
        assert note.read_text() == 'Baseline note\n'
        assert run(['git', 'rev-list', '--count', 'HEAD'], folder).strip() == '3'
        run(['git', 'switch', '-c', 'feature/wording'], folder)
        note.write_text('Feature wording\n')
        run(['git', 'add', 'note.txt'], folder)
        run(['git', 'commit', '-m', 'Feature'], folder)
        run(['git', 'switch', 'main'], folder)
        note.write_text('Main wording\n')
        run(['git', 'add', 'note.txt'], folder)
        run(['git', 'commit', '-m', 'Main'], folder)
        run(['git', 'merge', 'feature/wording'], folder, expected=1)
        assert '<<<<<<<' in note.read_text()
        note.write_text('Main and feature agree on the final wording\n')
        run(['git', 'add', 'note.txt'], folder)
        run(['git', 'commit', '-m', 'Resolve'], folder)
        assert not run(['git', 'status', '--short'], folder)


def check_snapshot(lesson):
    branch = lesson['branch']
    available = run(['git', 'for-each-ref', '--format=%(refname)']).splitlines()
    choices = ['refs/heads/' + branch, 'refs/remotes/origin/' + branch]
    ref = next((c for c in choices if c in available), None)
    assert ref, f'Missing {branch}; fetch all branches first'
    with tempfile.TemporaryDirectory(prefix='act1-snapshot-') as tmp:
        folder = Path(tmp)
        archive = subprocess.run(['git', 'archive', ref], cwd=ROOT, stdout=subprocess.PIPE, check=True).stdout
        subprocess.run(['tar', '-xf', '-', '-C', str(folder)], input=archive, check=True)
        check_docs(folder)
        checkpoint = json.loads((folder / 'checkpoint.json').read_text())
        assert checkpoint['lesson'] == lesson['id']
        assert (folder / 'examples/navigation/notes/checkpoint.txt').exists()
        assert (folder / 'requirements.txt').read_text().strip() == 'pytest==8.4.2'
        if lesson['id'] < 4:
            assert not (folder / 'app/operations.py').exists()
        else:
            output = run([sys.executable, '-m', 'pytest', '-q'], folder)
            assert f"{lesson['tests']} passed" in output, output
            operations = folder / 'app/operations.py'
            original = operations.read_text()
            operations.write_text(original.replace('return a - b', 'return a + b'))
            failure = run([sys.executable, '-m', 'pytest', '-q'], folder, expected=1)
            assert 'failed' in failure and 'AssertionError' in failure, failure
            operations.write_text(original)
        assert (folder / '.github/workflows/tests.yml').exists() == (lesson['id'] >= 7)
    print(f"Verified {branch}: {lesson['tests']} arithmetic tests")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'curriculum.json').read_text())
    assert len(manifest['lessons']) == 8
    assert sum(l['direct_minutes'] for l in manifest['lessons']) == 256
    print(f'Checked {check_docs(ROOT)} Markdown files and Python snippets')
    if args.full:
        for lesson in manifest['lessons']:
            check_snapshot(lesson)
        recovery_check()
        print('Recovery: unstage, revert, deliberate conflict and resolution verified')
    print('Course checks passed')


if __name__ == '__main__':
    main()
