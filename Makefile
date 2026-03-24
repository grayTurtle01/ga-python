fmt:
	black main.py tests.py

linter:
	pylint main.py tests.py
	
tests:
	pytest tests.py
