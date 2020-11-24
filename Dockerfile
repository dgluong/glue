FROM python:3.7.5-slim

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# COPY ./requirements.txt /app/requirements.txt
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# COPY . /app

ENTRYPOINT ["python"]

CMD [ "app.py" ]
