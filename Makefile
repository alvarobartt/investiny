.PHONY: quality style types tests

quality:
	black --check --target-version py39 --preview src/investiny tests
	isort --check-only src/investiny tests
	flake8 src/investiny tests

style:
	black --target-version py39 --preview src/investiny tests
	isort src/investiny tests

types:
	mypy src/investiny tests

tests:
	pytest tests/ --durations 0 -s
