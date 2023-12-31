run:
	make build
	python out/bundle.py --OO

build:
	make format
	python bundler.py --OO

format:
	ruff check src/ --config ruff.toml
	ruff format src/ --config ruff.toml

setup: requirements.txt
	pip install -r requirements.txt