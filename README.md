# gh-contrib-demo

Very loose scaffold for a Python library around GitHub contribution analysis.

There are intentionally almost no restrictions.
Only one concrete example is kept: `Repo.from_json`.

## Setup

```sh
uv sync
```

## Run checks

```sh
uv run pytest
uv run ruff check .
```
