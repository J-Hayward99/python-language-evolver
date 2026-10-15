.PHONY: help install run dev test lint format clean docker-build docker-run

APP  ?= app.main:app
HOST ?= 0.0.0.0
PORT ?= 8000

help:  ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies from pyproject.toml / uv.lock
	uv sync

run:  ## Run the app (production-style)
	uv run uvicorn $(APP) --host $(HOST) --port $(PORT)

dev:  ## Run with auto-reload
	uv run uvicorn $(APP) --host $(HOST) --port $(PORT) --reload

test:  ## Run tests
	uv run pytest -v

lint:  ## Lint code
	uv run ruff check .

format:  ## Format code
	uv run ruff format .

clean:  ## Remove caches and virtualenv
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .venv

docker-build:  ## Build Docker image
	docker build -t fastapi-app .

docker-run:  ## Run Docker container
	docker run --rm -p $(PORT):8000 fastapi-app