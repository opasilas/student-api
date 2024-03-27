# Makefile for managing Flask application

.PHONY: build test

build:
	@echo "Building app container"
	@echo "Building db container"

	docker-compose up --build -d

# setup:
# 	@echo "Setting up virtual environment..."
# 	python3 -m venv venv
# 	@echo "Activating virtual environment..."
# 	. venv/bin/activate; \
# 	pip install --upgrade pip; \
# 	pip install -r requirements.txt
# 	# @echo "Running database migrations..."
# 	# flask db upgrade

# run:
# 	. venv/bin/activate; \
# 	FLASK_APP=run.py flask run --no-reload --host=127.0.0.1 --port=5000 &
# 	sleep 5 # Wait for Flask app to start up
# 	curl http://127.0.0.1:5000/api/v1/students # Perform a test request
# 	# kill $(pgrep -f 'flask run') # Terminate Flask app


# test:
# 	. venv/bin/activate; \
# 	pytest tests

test:	
	docker ps
	
	docker exec -i student-api_student-api-app_1 sh
	sudo apt-get update
	sudo apt-get install curl
	curl http://localhost:5000/api/v1/students/health 
# clean:
# 	@echo "Cleaning up..."
# 	rm -rf venv
