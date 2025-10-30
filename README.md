# A simple website, but we have big plans

Cloning the repository.

Go to the repository folder.

### If you don't have Docker on your computer, you should install it first.

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