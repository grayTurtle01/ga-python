fmt:
	ruff format .

linter:
	pylint main.py test_fizzbuzz.py
	
tests:
	pytest .
