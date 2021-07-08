clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']

init_db:
	FLASK_APP=little_notes/app.py flask create-db

db_upgrade:
	FLASK_APP=little_notes/app.py flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=little_notes

format:
	isort little_notes/*
	isort tests/*
	black -l 79 little_notes/*
	black -l 79 tests/*

run:
	FLASK_APP=little_notes/app.py FLASK_ENV=development flask run