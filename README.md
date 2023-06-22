# Orientation Project - Python

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Pylint](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pylint.yml/badge.svg)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pylint.yml)
[![Pyright](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pyright.yml/badge.svg)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pyright.yml)
[![Pytest](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pytest.yml/badge.svg)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pytest.yml)

Refer to the Fellowship LMS for information!

## Setup

You can install Poetry by running the following. This command assumes you have Python installed. Substitute `python` to `python3` if necessary. More detailed instructions can be found [here](https://python-poetry.org/docs/#installing-with-the-official-installer).

```bash
curl -sSL https://install.python-poetry.org | python -
```

Once Poetry is installed, you can install the dependencies for this project by running the following.

```bash
poetry install
```

## Development

Here are a lists of development commands.

### Adding Dependencies

You can add dependencies by running the following. Changes will be reflected in [pyproject.toml](pyproject.toml) and [poetry.lock](poetry.lock).

```bash
poetry add <package>
```

### Removing Dependencies

You can remove dependencies by running the following. Changes will be reflected in [pyproject.toml](pyproject.toml) and [poetry.lock](poetry.lock).

```bash
poetry remove <package>
```

### Run

```bash
flask run
```

### Run Tests

```bash
pytest test_pytest.py
```

### Run Linter

```bash
pylint *.py
```

### Run Typechecker

```bash
pyright
```
