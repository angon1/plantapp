FROM python:3.10

#workdir
WORKDIR /plantapp

COPY ./requirements.txt /plantapp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /plantapp/requirements.txt

COPY ./plantapp /plantapp/plantapp

#execute command
CMD ["python", "-m", "plantapp"]
