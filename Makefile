.ONESHELL:

.PHONY: clean install run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -iname '__pycache__' -delete
	find . -type f -name '*.log' -delete

install:
	python -m venv venv; \
	venv/bin/activate; \
	pip install -e .['dev'];

tests:
	. venv/bin/activate; \
	python manage.py test

run:
    venv/bin/activate; \
	export FLASK_ENV=development && \
	export FLASK_APP=bacchus/app.py && \
	flask run

all: clean install run