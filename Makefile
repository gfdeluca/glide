.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

tests:
	. venv/bin/activate; \
	python manage.py test

coverage:
	. venv/bin/activate; \
	coverage run manage.py test; \
	coverage html

production:
	. venv/bin/activate; \
	python setup.py bdist_wheel

run:
	. venv/bin/activate; \
	python manage.py run

all: clean install tests coverage run
