run:
	make build
	python out/bundle.py --enable-big-digits=15 --OO --enable-optimizations --enable-bolt

build:
	python build.py --enable-big-digits=15 --OO --enable-optimizations --enable-bolt

exe:
	python distribute.py --enable-big-digits=15 --OO --enable-optimizations --enable-bolt

setup: requirements.txt
	pip install -r requirements.txt