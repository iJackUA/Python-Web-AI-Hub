# Python Web AI Hub

> Python learning and experimental playground
> Brief idea: Web site that allows to index and "ask question via AI assistant" to other web sites, text/pdf documents, YouTube video subtitles and potentially other textual media.

## Running in dev mode

### Dev machine without virtualisation

- Install `pyenv` <https://github.com/pyenv/pyenv> to manage Python versions
- `curl https://pyenv.run | bash` (do not forget to update bash/zsh .rc files)
- `pyenv install`
- [Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) to manage Dependencies and Envs
- `curl -sSL https://install.python-poetry.org | python3 -`
- `poetry self add poetry-auto-export && poetry self add poetry-plugin-export` [add Poetry plugins for requirements.txt autoexport](https://github.com/Ddedalus/poetry-auto-export)
- `poetry install` install dependencies

### Running web app

- `poetry run python manage.py runserver`

## Useful commands

- `poetry add pendulum` || `poetry add pendulum@~2.0.5` add package (latests || fixed versions)
- `poetry export -f requirements.txt --output requirements.txt` manual export dependencies
