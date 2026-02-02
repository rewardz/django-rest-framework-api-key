.PHONY: help test_install_django18 test_with_coverage build_with_django_18 build_with_django_111

# Default target
help:
	@echo "Available commands:"
	@echo "  make install_django18   - Install Test dependencies for django 1.8"
	@echo "  make test_with_coverage      - Run all test cases"
	@echo "  make build_with_django_18 - Run and Build docker image with django 1.8"
	@echo "  make build_with_django_111 - Run and Build docker image with django 1.11"

# Install dependencies
install_django18:
	@echo "Installing test dependencies for django 1.8 ..."
	pip install -r requirements/django18/requirements-testing.txt

# Run tests
test_with_coverage:
	@echo "Running tests..."
	python runtests.py

# Start build with django version 1.8 and start container
build_with_django_18:
	@echo "Starting Docker build..."
	docker build -t django-rest-framework-api-key --build-arg REQUIREMENTS_FILE=requirements/django18/requirements-testing.txt .
	docker run -it --rm django-rest-framework-api-key

# Start build with django version 1.11 and start container
build_with_django_111:
	@echo "Starting Docker build..."
	docker build -t django-rest-framework-api-key-111 --build-arg REQUIREMENTS_FILE=requirements/django18/requirements-testing.txt .
	docker run -it --rm django-rest-framework-api-key-111
