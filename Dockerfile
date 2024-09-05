FROM python:3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir pytest allure-pytest

COPY . .

RUN apt-get update && apt-get install -y make

