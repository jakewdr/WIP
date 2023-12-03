run:
	make build
	python out/bundle.py -O

build:
	python build.py

setup: requirements.txt
	pip install -r requirements.txt