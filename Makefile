run:
	make build
	python out/bundle.py --OO

build:
	python build.py --enable-big-digits=15 --OO

exe:
	python distribute.py --enable-big-digits=15 --OO

setup: requirements.txt
	pip install -r requirements.txt