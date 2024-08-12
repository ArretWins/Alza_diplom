FROM python:3-slim
WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .