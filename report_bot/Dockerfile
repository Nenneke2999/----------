FROM python:3.11

WORKDIR /telegrambot

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --use-pep517


COPY . .