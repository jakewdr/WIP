run:
	make build
	python out/bundle.py --OO

build:
	python build.py --OO

setup: requirements.txt
	pip install -r requirements.txt