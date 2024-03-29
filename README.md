## fixtup-sqlalchemy

**This package is under construction and should not be used in any product**

[![ci](https://github.com/FabienArcellier/fixtup-sqlalchemy/actions/workflows/main.yml/badge.svg)](https://github.com/FabienArcellier//fixtup-sqlalchemy/actions/workflows/main.yml)

[Soon]

## Getting started

Install plugin in python environment

```
pip install fixtup-sqlalchemy
```

Activate the plugin in the fixtup configuration

*pyproject.toml*
```
[tools.fixtup]
fixtures = "fixtures"
plugins = [
    "fixtup_sqlalchemy.plugin"
]
```

*setup.cfg*
```
[fixtup]
fixtures = tests/fixtures/fixtup
plugins=
    fixtup_sqlalchemy.plugin
```

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/fixtup-sqlalchemy.git
```

## Usage

[Soon]

## Developper guideline

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
pipenv install --dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
pipenv update
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
pipenv shell
```

### Run the continuous integration process

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
$ pipenv shell
$ alfred ci
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018-2022 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
