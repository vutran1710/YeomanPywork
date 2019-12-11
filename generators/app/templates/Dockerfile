FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --deploy

CMD STAGE=production pipenv run app
