# Python project template

A Python project template repository.

## Features
- [VS Code .devcontainer](https://code.visualstudio.com/docs/remote/containers) configuration that installs commonly used VS Code extensions.
- [Dockerfile](https://docs.docker.com/engine/reference/builder/) with Python and the local package with DEV dependencies installed.
- [pyproject.toml package configuration](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) with optional DEV and TEST dependency lists.
- [Pytest](https://github.com/boxed/pytest-readme) template setup with code [coverage](https://coverage.readthedocs.io/en/6.4.2/) reporting.
- [Pre-commit hooks](https://pre-commit.com) configuration with excellent hooks for better code quality and safety.
- [Black](https://github.com/psf/black) code formatting.
- [GitHub Actions](https://docs.github.com/en/actions) configuration for automated testing and building on GitHub.
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/index.html) configuration for automated testing and building on GitLub.
- [.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore) template
modified from GitHub.
- README template from [makeareadme](https://www.makeareadme.com/).
- LICENSE file.

## Usage
Clone this repository to your local machine and rename the all the instances of "python_project_template" and "python-project-template" to your project name.

```bash
git clone https://github.com/jacoverster/python-project-template
```

Update the pyroject.toml, README.md, LICENSE, etc.

Create a git repo for your project and add the files to your repo:

```bash
git init
git add *
git commit -m "initial commit"
git branch -M main
git remote add origin https://link-to-your-git-repo
git push -u origin main
```

To run pytest with code coverage

```bash
coverage run -m pytest
coverage report
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
