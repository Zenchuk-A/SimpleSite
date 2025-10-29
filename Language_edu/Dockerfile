# FROM python:3.12

# WORKDIR /app

# RUN pip install gunicorn==23.0.0

# COPY requirements.txt .

# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "Language_edu.wsgi"]


FROM python:3.12

WORKDIR /app

# Установка зависимостей для PostgreSQL
# RUN apt-get update && apt-get install -y \
#     postgresql-client \
#     && rm -rf /var/lib/apt/lists/*

# Копирование requirements и установка Python-зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# Копирование проекта
COPY . .

# Создание директории для медиа
RUN mkdir -p media

# EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]