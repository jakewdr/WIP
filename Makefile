run & start:
	make build
	python out/bundle.py --OO

build & bundle:
	make format
	python bundler.py --OO

format:
	ruff check --fix --no-unsafe-fixes --quiet src/ --config ruff.toml
	ruff format --quiet src/ --config ruff.toml

setup: requirements.txt
	pip install -r requirements.txt