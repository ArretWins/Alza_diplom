FROM python:3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir pytest allure-pytest

RUN apt-get install -y openjdk-11-jre wget unzip \
    && wget https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.zip -O /tmp/allure.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure

COPY . .

RUN apt-get update && apt-get install -y make

CMD ["make", "test-all"]
CMD ["make", "test-api"]
CMD ["make", "test-basket"]
CMD ["make", "test-delivery"]
CMD ["make", "test-login"]
CMD ["make", "test-main"]
CMD ["make", "test-product"]
CMD ["make", "test-contact"]
CMD ["make", "clean-allure"]


ENTRYPOINT ["allure", "serve", "/app/allure-results"]