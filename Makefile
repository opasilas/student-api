# Makefile for managing Flask application

.PHONY: setup run test clean

setup:
	@echo "Setting up virtual environment..."
	python3 -m venv venv
	@echo "Activating virtual environment..."
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt
	@echo "Running database migrations..."
	flask db upgrade

run:
	. student-api-venv/bin/activate; \
	FLASK_APP=run.py flask run

test:
	. venv/bin/activate; \
	pytest tests

clean:
	@echo "Cleaning up..."
	rm -rf venv
