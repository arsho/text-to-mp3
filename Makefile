#!/bin/bash

activate-virtualenv-run-app:
	. venv/bin/activate; \
	venv/bin/python app.py; \

create-virtualenv-install-requirements:
	virtualenv venv -p python3 --no-site-packages; \
	. venv/bin/activate; \
	venv/bin/pip install -r requirements.txt; \
	
install: create-virtualenv-install-requirements

run: activate-virtualenv-run-app
