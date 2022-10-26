REPO_NAME = radai
PYTHON_VERSION = 3.9.7

.python-version:
	pyenv install --skip-existing $(PYTHON_VERSION)
	pyenv virtualenv --force $(PYTHON_VERSION) $(REPO_NAME)
	pyenv local $(REPO_NAME)

venv: .python-version

.PHONY: develop
develop: venv
	pip install -U pip
	pip install -e .

.PHONY: dev-deps
dev-deps: venv
	pip install --upgrade \
		bandit \
		flake8 \
		ipython \
		isort \
		mypy \
		pre-commit \
		pytest \
		pytest-mock \
		safety

.PHONY: init
init: develop dev-deps
	pre-commit install

.PHONY: test
test:
	pytest

.PHONY: clean-venv
clean-venv:
	pyenv uninstall --force $(REPO_NAME)

.PHONY: deinit
deinit: clean-venv
	pyenv local --unset
