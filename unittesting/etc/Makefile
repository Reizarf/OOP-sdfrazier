
run:
	python3 main.py

mypy:
	mypy --strict 

lt1:
#I can't figure out why these tests aren't working - they run fine
#outside of Makefile...?
	@echo "test 1 complete"
	@cat ans/1.in | python3 main.py | diff - ans/1.ans
	
	
#same here
lt2:
	cat ans/2.in | python3 main.py | diff - ans/2.ans
	echo "tesst 2 complete"

uml:
	java -jar ~/plantuml-1.2023.1.jar docs/*.plantuml

pdoc:
	#pdoc --html main.py morse.py localhost:8080 #this is not working
	pdoc --force --html -o docs main.py morse.py