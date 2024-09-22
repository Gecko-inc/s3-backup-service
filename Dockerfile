FROM python:3.11.0-slim

# Устанавливаем необходимые утилиты
RUN apt-get update && apt-get install -y wget gnupg2 lsb-release

# Добавляем репозиторий PostgreSQL
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Добавляем ключ репозитория
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Обновляем список пакетов и устанавливаем PostgreSQL клиент версии 14
RUN apt-get update && apt-get install -y postgresql-client-14

# Рабочая директория
WORKDIR /app

# Копируем все файлы
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Команда запуска Python
CMD ["python", "main.py"]
