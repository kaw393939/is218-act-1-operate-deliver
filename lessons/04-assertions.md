# Lesson 04: Make an assertion that can fail

[Act home](../README.md) · [Previous](./03-environment.md) · [Next](./05-focused-commits.md)

**Week 2, meeting 2 · 80 minutes · 30 minutes direct practice**

[Worked checkpoint](https://github.com/kaw393939/is218-act-1-operate-deliver/tree/lesson/04-assertions) · [AI boundaries](../docs/assistance.md)


## By the end you can

- Implement the stated ordered arithmetic contract.
- Write six explicit tests with independently expected results.
- Interpret an observed assertion failure and repair the defective behavior.

**Opening retrieval (0–10):** What is the independent expected value of subtract(2, 5)?

## The problem: running without crashing does not establish correctness

A function returns a number. Was it the right number? A contract and independently expected examples let us decide.

## Read and predict (0–25)

Our contract accepts ordinary finite Python `int`/`float` operands: `add(a, b)` returns their sum; `subtract(a, b)` returns `a - b`. No CLI, classes, input validation, pandas, or design patterns are required in Act 1. Subtraction is ordered: `subtract(2, 5)` is `-3`.

Arrange prepares data; Act calls the function; Assert compares the observation with an expectation computed independently. Essential vocabulary: contract, assertion, Arrange–Act–Assert.

## Direct lab (25–55): build and observe a real failure

In your student project create folders `app` and `tests`, plus empty `app/__init__.py`. In `app/operations.py` write:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return a minus b; operand order matters."""
    return a - b
```

Create `tests/test_operations.py`; this is the worked example, then add your own independent cases:

```python
from app.operations import add, subtract


def test_add_positive():
    # Arrange
    a, b = 2, 3
    expected = 5
    # Act
    result = add(a, b)
    # Assert
    assert result == expected


def test_subtract_positive():
    a, b = 7, 2
    expected = 5
    result = subtract(a, b)
    assert result == expected
```

Activate your environment, run `python -m pytest -q` from root, and observe two passing tests. Add four explicit AAA tests: addition with negative operands, addition with a zero operand, subtraction with negative operands, and subtraction yielding a negative result. Choose your own small integers and calculate expected results before running. The reference branch has six tests for comparison **after** your attempt.

In a disposable practice change, temporarily make `subtract` return `a + b`. Run the tests. At least the worked subtraction case must fail (`9` observed versus `5` expected). Record the assertion excerpt. Repair the function according to the contract, keeping the independent expected value. Rerun: six tests should pass. Do not commit the deliberate defect as your final state.

**Independent variation:** explain which of your cases detects reversed subtraction operands and why. If none does, add one.

## Critique (55–75)

Critique `assert add(2, 3) == add(2, 3)`: it can pass even when addition is wrong. Explain why an expected result is not simply whatever the function returns. Outside direct practice, ask AI to review the coverage of your six cases and verify one proposed gap yourself.

## Exit evidence (75–80)

Six passing tests, one observed wrong-result failure, its diagnosis, and the submitted commit SHA. Complete [Week 2](../assignments/week-2.md).

## Stuck or ahead?

Import failure and assertion failure occur at different stages. Confirm `app/__init__.py`, working directory, and selected interpreter before changing arithmetic. Faster learners add an exactly representable decimal case such as `0.5 + 0.25`; avoid treating all floating-point sums as exact decimal arithmetic.

**Instructor checkpoint:** ask a student to explain an assertion's observed and expected values and why changing the expectation would be wrong here.
