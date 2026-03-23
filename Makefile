fmt:
	black zandbox.py tests.py

linter:
	pylint zandbox.py tests.py
	
tests:
	python3 -m unittest tests.py
