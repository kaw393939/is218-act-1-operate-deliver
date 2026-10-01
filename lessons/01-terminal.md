# Lesson 01: Find your bearings in the terminal

[Act home](../README.md) · [Next](./02-github.md)

**Week 1, meeting 1 · 80 minutes · 30 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/01-terminal) · [AI boundaries](../docs/assistance.md)


## The problem: the right command in the wrong folder

An editor shows your project, but the terminal is somewhere else. Predict where `notes.txt` would land before creating it. Your goal is to explain locations without relying on an AI agent's guess.

## Read and predict (0–25 minutes)

A terminal displays an interaction; a shell interprets commands. Your working directory determines relative paths. An absolute path starts from the filesystem root; a relative path starts from a context. `..` means parent, not “undo.”

Ask: if you start in `is218-labs`, enter `navigation`, then enter `notes`, what does `../README.md` refer to? Sketch it before running commands. Open the [command reference](../docs/commands.md).

## Direct lab (25–55): make paths visible

Use macOS Terminal or WSL Ubuntu. Start in your home folder; if an `is218-labs/navigation` folder already exists, choose a new unused name and adapt the path. Do not overwrite earlier work.

```bash
cd ~
mkdir -p is218-labs/navigation/notes
cd is218-labs/navigation
printf 'My terminal practice\n' > README.md
printf 'I predict before running commands.\n' > notes/checkpoint.txt
pwd
ls -a
cat README.md
cd notes
pwd
cat ../README.md
cat checkpoint.txt
cd ..
```

The two `pwd` outputs should differ by a trailing `/notes`. Reading `../README.md` from `notes` prints `My terminal practice`. The second file prints `I predict before running commands.` Your home path will differ from the instructor's.

Create this tree in your notes:

```text
navigation/
├── README.md
└── notes/
    └── checkpoint.txt
```

Open the folder in your editor. Change the checkpoint sentence, save it, and reread it with `cat notes/checkpoint.txt`. If the old text remains, investigate whether the editor and terminal refer to the same folder.

**Independent variation:** create `notes/questions.txt` in the editor. From the parent of `navigation`, predict and then use the relative path to read it. Explain why its path differs from the one used inside `navigation`.

## Critique (55–75)

A partner names a starting directory; you explain the path to the checkpoint file. Swap. Outside direct practice, ask AI to explain the difference between shell and terminal, then connect its explanation to what you observed. Reject any claim that opening an editor automatically changes every terminal's directory.

## Exit evidence (75–80)

Record your tree, actual working directory, and explanations of three commands. Answer: “Which command inspected state, which changed state, and what did I check afterward?” This becomes part of [Week 1](../assignments/week-1.md).

## Stuck or ahead?

`No such file` is evidence about a path, not proof the file vanished. Use `pwd` and `ls` at the intended parent. Faster learners repeat the path explanation with a folder name containing spaces and quote the path. This is optional.

**Instructor checkpoint:** ask a student to locate an existing file from two starting directories without copying a path from the editor. Accept equivalent safe commands, not a memorized sequence.
