uml:
	java -jar ~/Desktop-c/plantuml-1.2023.1.jar docs/doc.plantuml
	java -jar ~/Desktop-c/plantuml-1.2023.1.jar docs/doc2.plantuml

run:
	python3 main.py

pdoc:
	pdoc --html docs/ main.py number_list.py

lt1:
	cat docs/1.in | python3 kattis_func.py | diff - docs/1.ans

lt2:
	cat docs/2.in | python3 kattis_func.py | diff - docs/2.ans
