# === Configuration ===
MAKEFLAGS += --silent
make:
	cat -n ./Makefile

# === Dev ===
.PHONY: lint
lint:
	poetry run ruff check ./snipstr ./tests \
	&& poetry run ruff format ./snipstr ./tests \
	&& poetry run flake8 ./snipstr \
	&& poetry run mypy ./snipstr --no-pretty \
	&& poetry run codespell snipstr tests README.md CONTRIBUTING.md

.PHONY: tests
tests:
	poetry run pytest ./tests/

.PHONY: cov
cov:
	poetry run pytest --cov=snipstr ./tests

.PHONY: all
all:
	make lint && make tests

# === Aliases ===
l: lint
t: test
a: all
