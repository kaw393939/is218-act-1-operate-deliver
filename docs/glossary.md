# Vocabulary for owning a change

[Act home](../README.md)

Use these terms to make a concrete claim about a file, command, responsibility, or check. Naming a term without pointing to evidence is not enough.

| Term | Meaning in this act | Useful question |
| --- | --- | --- |
| Shell / terminal | Shell interprets commands; terminal presents the interaction | Which shell syntax am I using? |
| Working directory | Directory relative paths start from | Where will this file be created? |
| Absolute / relative path | Complete location / location from a starting directory | Relative to what? |
| Repository | Files plus tracked revision history | Which repository am I modifying? |
| Working tree / staging area / commit | Current files / proposed next snapshot / recorded snapshot | Which state contains this edit? |
| Remote / origin | Named location for exchanging commits / conventional remote name | Whose repository is this URL? |
| Branch / pull request | Name pointing to a revision / proposed integration with review | Is this work merely published or integrated? |
| Interpreter | Program executing Python | Which executable ran the tests? |
| Virtual environment | Project-specific interpreter environment and packages | Can another machine recreate it? |
| Dependency | External package the project needs | Is its version recorded? |
| Contract | Agreed input, output, and behavior | What should subtract(2, 5) return? |
| Assertion | Check comparing observation to expectation | Did I calculate expected independently? |
| Arrange–Act–Assert (AAA) | Prepare inputs, call behavior, compare result | What behavior does this test establish? |
| Regression | Previously supported behavior breaks after a change | Which old test guards it? |
| Reproducibility | Another person can recreate specified work/checks | Which revision and environment? |
| CI | Automated checks on a hosted runner | Which job and commit actually ran? |
| Separation of concerns | Give different responsibilities distinct homes | Why are arithmetic and tests in different files? |
| DRY: don't repeat yourself | Give a piece of knowledge one authoritative home | Am I copying behavior or independently stating a test expectation? |
| KISS | Keep a solution as simple as its requirements allow | Does this tiny function need a class yet? |
| YAGNI | Avoid building speculative capabilities | Did anyone require a web UI in Act 1? |
| Cohesion / coupling | Related responsibilities together / dependence between parts | Can a test use arithmetic without starting an interface? |
| Verification / limitation | Evidence that a claim holds / what that evidence leaves open | Does green CI prove local environment use? |

## Principles before patterns

A principle is guidance for deciding; a pattern is a named recurring arrangement of responsibilities. We will study creational, structural, and behavioral patterns in Act 2. Here we practice the language that makes those discussions possible. Functions and tests are enough for this act's scope.

DRY does not mean deriving expected values by calling the same function under test. `assert add(2, 3) == add(2, 3)` repeats a call without checking its meaning. `assert add(2, 3) == 5` uses an independent expectation. Repeating a small explicit test structure can make independent evidence easier to read.

Separation of concerns does not mean “one file per line.” Our arithmetic module owns calculations; the test module owns examples of the contract; the workflow owns automated execution. Each home has a reason.

## Transfer to AI and other languages

“Add a mixed-sign regression case without changing the public function signature” is more precise than “make it better.” The words contract, regression, responsibility, and reproducibility remain useful in JavaScript or Java even though the syntax and tools change.

Practice: point to one example of separation of concerns; identify one CI claim that is too broad; rewrite an ambiguous AI request using two terms and an acceptance check.
