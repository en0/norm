# Not an ORM

A implementation of the Generic Repository

## Quick Start

### Prerequisites

- Ensure you have Python 3.10 or newer installed on your machine
- Install [Poetry](https://python-poetry.org/docs/#installing-with-pipx) for dependency management.

__For Arch__

```bash
sudo pacman -S python-poetry
```

### Setup

1. __Clone the Repository__

Clone the repository to your local machine:

```bash
git clone https://github.com/en0/not_an_orm.git
cd not_an_orm
```

2. __Install dependencies__

Use Poetry to install the project dependencies:

```bash
poetry install --with dev
```

This command will create a virtual environment and install all the required packages as specified in
the pyproject.toml

3. __Activate the Virtual Environment__

You can activate the virtual environment created by Poetry:

```bash
$(poetry env activate)
```

Alternatively, you can run commands directly within the virtual environment using:

```bash
poetry run <command>
```

### Running Tests

To run tests using pytest, you can simply execute:

```bash
pytest
```

Alternatively, you can use pytest-watch to run whenever you save changes:

```bash
ptw
```

This command will monitor your project files and re-run the tests each time a file is saved.

## Contribute

TBD...
