setup:
	rm -rf venv
	sudo apt-get install python-pip libpq-dev
	pip install virtualenv
	virtualenv --python=python2.7 venv
	. venv/bin/activate
	pip install -e .
	python init_db.py
run:
	python app.py

test:
	pytest tests