run & start:
	make build
	python out/bundle.py --OO

build & bundle:
	ruff check --fix bundler.py --config ruff.toml
	ruff format bundler.py --config ruff.toml
	make format
	python bundler.py --OO

format:
	ruff check --fix src/ --config ruff.toml
	ruff format src/ --config ruff.toml

setup: requirements.txt
	pip install -r requirements.txt
	make format