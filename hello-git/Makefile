PLANTUML=java -jar ~/plantuml.jar

all: static_type_check test run create_docs

create_docs:
	mkdir docs
	pdoc -o docs --html hello.py
	pdoc -o docs --html main.py

static_type_check:
	mypy --strict --disallow-untyped-defs hello.py
	mypy --strict --disallow-untyped-defs main.py
	@echo "Type checking passed!"

run:
	@python3 main.py

test:
	python3 main.py | diff - data/1.ans

create_uml:
	java -jar ~/plantuml.jar uml/hello.plantuml
	$(PLANTUML) uml/
