
# pull official base image
FROM python:3.6-alpine

# set work directory
WORKDIR /usr/src/telegram

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add sqlite

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/telegram/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/telegram/
