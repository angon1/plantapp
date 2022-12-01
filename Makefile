SHELL := /bin/bash



install:
	python3 -m venv venv
	source venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt && \
	pre-commit install


clean:
	rm -fr venv

push:
	source venv/bin/activate && \
	git add . && \
	git commit && \
	git push
