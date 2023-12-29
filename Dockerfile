FROM python:3.10-alpine

WORKDIR /app

RUN apk update && apk add --no-cache --virtual bash git gcc g++

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/

RUN python -m pip install requirements.txt

COPY . /app

CMD ["python", "main.py"]