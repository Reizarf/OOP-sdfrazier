run:
	python3 main.py

mypy:
	mypy --strict main.py
	

localtest:
	cat ans/1.in | python3 main.py | diff - ans/1.ans
	echo "tests complete"
	
uml:
	java -jar ~/Desktop/plantuml-1.2023.1.jar docs/doc.plantuml

pdoc:
	pdoc --http --force -o out.html polygonarea.py main.py

