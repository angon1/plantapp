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

run:
	source venv/bin/activate && \
	python -m plantapp

docker_build:
	docker build -t plantapp_img .

docker_run:
	docker run -d --name plantapp -p 8888:8888 plantapp_img
