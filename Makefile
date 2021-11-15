install:
	pip install -e .['dev']

run:
	export FLASK_ENV=development && \
	export FLASK_APP=bacchus/app.py && \
	flask run