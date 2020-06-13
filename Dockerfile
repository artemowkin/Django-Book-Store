FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /bookstore

COPY Pipfile Pipfile.lock /bookstore/
RUN pip install pipenv && pipenv install --system

COPY . /bookstore/
