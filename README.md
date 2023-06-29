# Orientation Project - Python

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Pylint](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pylint.yml/badge.svg)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pylint.yml)
[![Pyright](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pyright.yml/badge.svg)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pyright.yml)
[![Pytest](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pytest.yml/badge.svg)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/actions/workflows/pytest.yml)

Refer to the Fellowship LMS for information!


## API Documentation
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/10259207-c8e69b39-9dda-4b75-a761-cf7322130902?action=collection%2Ffork&collection-url=entityId%3D10259207-c8e69b39-9dda-4b75-a761-cf7322130902%26entityType%3Dcollection%26workspaceId%3D5e5a6553-99d8-41e1-91a7-d8e7d4504230)

##### You can also find the API documentation here, [23.SUM.B.1 MLH Fellowship orientation project API documentation](https://documenter.getpostman.com/view/10259207/2s93zB41EG).
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


### Activating virutal environment

After installing poetry, the virtual environment is automatically created and activated.
But in case it is not activated, run the following command to activate it.

```bash
poetry shell
```

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

### Contributors
[![](https://contrib.rocks/image?repo=MLH-Fellowship/orientation-project-python-23.SUM.B.1)](https://github.com/MLH-Fellowship/orientation-project-python-23.SUM.B.1/graphs/contributors)
