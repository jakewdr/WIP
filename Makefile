run & start:
	make build
	python out/bundle.py --OO

build & bundle:
	
	make format
	python bundler.py --OO

format:
	ruff check --fix src/ --config ruff.toml
	ruff format src/ --config ruff.toml

fix:
	make setup
	ruff check --fix bundler.py --config ruff.toml
	ruff format bundler.py --config ruff.toml
	make format

setup: requirements.txt
	pip install -r requirements.txt