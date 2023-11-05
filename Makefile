BUILD_DIR=pythonseer

all:
	rm -rf dist
	poetry cache clear _default_cache --all  --no-interaction
	poetry cache clear PyPI --all  --no-interaction
	poetry check
	poetry run whispers $(BUILD_DIR) # Check for security issues
	poetry run tartufo scan-local-repo .
	poetry run vulture --min-confidence 100 $(BUILD_DIR)
	poetry run ruff format $(BUILD_DIR)
	poetry run pytest --cov --cov-fail-under=50

setup:
	python3 -m pip install pipx
	python3 -m pipx ensurepath
	pipx install poetry
	poetry install

install:
	pip install . --upgrade
