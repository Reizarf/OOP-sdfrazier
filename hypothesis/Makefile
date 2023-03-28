run:
	python3 main.py

mypy:
	mypy --strict main.py

lt1:
	cat docs/1.in | python3 main.py | diff - docs/1.ans
	@echo "test 1 successful"

lt2:
	cat docs/2.in | python3 main.py | diff - docs/2.ans
	@echo "test 2 successful"

uml:
	java -jar ~/Desktop-c/plantuml-1.2023.1.jar docs/doc.plantuml

pdoc:
	pdoc --html docs/ main.py title.py

coverage:
	coverage run -m unittest hypothesis/test_*