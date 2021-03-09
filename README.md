# Quizzes
Programming puzzles with a build-system to try out different
algorithms and development practices.

## Project Tree

[a relative link](cpp/)
 C++ demo(n) playground.
[a relative link](githooks/)
 Git hooks for running tests.
[a relative link](Makefile)
 The main entrypoint that drives building and testing.
[a relative link](python/)
 Python projects with packaging, tests and modules.


## Development

### Git hook

In absence of shared CI, it is recommended to install pre-commit
hook to run tests locally:

`ln -s "$(pwd)"/githooks/pre-commit.py .git/hooks/pre-commit`

### Build

`make`

### Run Tests

`make test`
