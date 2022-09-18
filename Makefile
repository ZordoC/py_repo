.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint test-unit test-integration test-e2e test-basic format

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

coverage: ## check code coverage quickly with the default Python

	coverage run --source pd_repo -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/pd_repo.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pd_repo
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

format:
	isort pd_repo tests
	black -l 100 pd_repo tests
	docformatter --in-place --recursive pd_repo tests

install: clean ## install the package to the active Python's site-packages
	python setup.py install

jupyter:
	jupyter notebook

lint: ## lint using flake8 + pylint
	flake8 pd_repo
	pylint  pd_repo

venv-dev:
	pip install -r requirements_dev.txt

venv:
	pip install -r requirements.txt

venv-all: venv-dev venv

tests-unit:
	pytest tests/unit

tests-integration:
	pytest test/integration

tests-e2e:
	pytest test/e2e

tests-basic: tests-unit test-integration

tests-all: tests-unit test-integration test-e2e

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .
