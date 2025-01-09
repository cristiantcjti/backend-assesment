PROJECT_NAME := backend_assesment_app
PYTHON_VERSION := 3.12.0
VENV_NAME := backend_assesment-$(PYTHON_VERSION)

include .env
export

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | sed -e 's/\(\:.*\#\#\)/\:\ /' | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -v -f {} +
	find . -name '*.pyo' -exec rm -v -f {} +
	find . -name '*~' -exec rm -v -f {} +
	find . -name '__pycache__' -exec rm -v -fr {} +

.clean-build: ## remove build artifacts
	rm -v -fr build/
	rm -v -fr dist/
	rm -v -fr .eggs/
	find . -name '*.egg-info' -exec rm -v -fr {} +
	find . -name '*.egg' -exec rm -v -f {} +

.clean-test: ## remove test and coverage artifacts
	rm -v -fr .tox/
	rm -v -f .coverage
	rm -v -fr htmlcov/
	rm -v -fr reports/
	rm -v -fr .pytest_cache/
	rm -v -f coverage.xml

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

setup-dev: ## install dev requirements
	poetry install --with dev

setup: ## install requirements
	poetry install --only main

create-venv: ## install python, create virtualenv and set virtualenv to current
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	python -m venv $(PYTHON_VERSION) $(VENV_NAME)
	$(VENV_NAME)/Scripts/pip install -U pip poetry

build: ## up all containers and building the project image
	docker-compose up -d --build

up: ## up all containers
	docker-compose up -d

down: ## down all containers
	docker-compose down
	docker-compose rm

recreate: down up ## recreate containers

migrations: ## create alembic migratrion file
	docker exec -it $(PROJECT_NAME) python manage.py makemigrations

migrate: ## run migratrion
	docker exec -it $(PROJECT_NAME) python manage.py migrate

shell: ## run shell
	docker exec -it $(PROJECT_NAME) python manage.py shell

logs: ## project logs on container
	docker logs $(PROJECT_NAME) --follow

test:  ## running test
	pytest -v

test-coverage: ## running test with coverage
	pytest -v --cov-config=pyproject.toml --cov=src --cov-report=term-missing --cov-report=xml --cov-fail-under=95
	sed -i 's/<source>.*<\/source>/<source>.\/<\/source>/g' coverage.xml

flake8: ## running flake8
	echo "Running flake8"
	flake8 src

bandit: ## running bandit
	echo "Running bandit"
	bandit -c pyproject.toml -r src

black:
	echo "Running black"
	black src

black-check:
	echo "Running black check"
	black --check src

code-convention: black-check flake8 bandit ## running black, flake8 and bandit

up-migrations-migrate: up migrations migrate
