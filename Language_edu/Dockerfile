FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn

COPY . .

RUN mkdir -p media

RUN python manage.py collectstatic --noinput

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "Language_edu.wsgi:application"]