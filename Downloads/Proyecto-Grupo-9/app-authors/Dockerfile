FROM python:3.11-alpine3.17
RUN mkdir /app-authors
COPY . /app-authors
WORKDIR /app-authors
RUN pip3 install pipenv
RUN pipenv install --system
