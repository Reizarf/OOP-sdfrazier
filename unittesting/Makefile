run:
	python3 palindrome.py

uml:
	java -jar ~/plantuml-1.2023.1.jar uml/*.plantuml

pdoc:
	pdoc --force --html -o docs palindrome.py unit_test.py

localtest:
	cat ans/1.in | python3 palindrome.py | diff - ans/1.ans
	cat ans/2.in | python3 palindrome.py | diff - ans/2.ans
	echo "Local tests passed :D"

more_test:
	cat ans/3.in | python3 palindrome.py | diff - ans/3.ans
