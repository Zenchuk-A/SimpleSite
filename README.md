# A simple website
### But we have big plans

Cloning the repository.

Go to the repository folder.

Creating Docker containers:
```
docker compose up -d --build
```

Applying migrations:
```
docker compose exec web python manage.py migrate
```

Creating a superuser:
```
docker compose exec web python manage.py createsuperuser
```