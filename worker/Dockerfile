# pull official base image
FROM python:3.6-alpine

# set work directory
WORKDIR /usr/src/worker

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/worker/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/worker/

ENTRYPOINT pipenv run celery worker --app tasks --loglevel=info
