run:
	make build
	python out/bundle.py --OO

build:
	make format
	python build.py --OO

winbuild:
	make format
	runas /user:Administrator "python build.py --OO"

format:
	ruff check src/ --config ruff.toml
	ruff format src/ --config ruff.toml

setup: requirements.txt
	pip install -r requirements.txt