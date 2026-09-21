.PHONY: setup test lint run frontend-install frontend-build

setup:
	uv sync
	cd frontend && pnpm install

run:
	uv run python manage.py runserver

test:
	uv run pytest -q

lint:
	uv run ruff check .

frontend-install:
	cd frontend && pnpm install

frontend-build:
	cd frontend && pnpm build
