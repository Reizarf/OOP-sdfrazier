pdoc:
	pdoc --html docs/ main.py fraction.py

run:
	python3 main.py

uml:
	java -jar ~/Desktop-c/plantuml-1.2023.1.jar docs/doc.plantuml

mypy:
	mypy fraction.py main.py

lt1:
	cat docs/1.in | python3 main.py | diff - docs/1.ans
	@echo "test 1 successful"

lt2:
	cat docs/2.in | python3 main.py | diff - docs/2.ans
	@echo "test 2 successful"