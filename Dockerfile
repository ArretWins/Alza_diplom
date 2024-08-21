# Используем официальный Python-образ, оптимизированный по размеру
FROM python:3-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только requirements.txt перед установкой зависимостей
COPY requirements.txt .

# Устанавливаем зависимости с отключением кеширования для экономии места
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем зависимости для Allure и тестов (если есть)
RUN pip install --no-cache-dir pytest allure-pytest

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
