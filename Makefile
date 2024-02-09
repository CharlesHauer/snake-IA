PYTHON = python3
PIP = pip

run:
	@echo "Running main.py..."
	$(PYTHON) main.py

clean:
	@echo "Cleaning up..."
	rm -rf tests/__pycache__ .pytest_cache snake_game/__pycache__


test:
	@echo "Running tests..."
	pytest

build:
	@echo "Building project..."
	$(PIP) install -r requirements.txt
	make run

.PHONY: clean run test