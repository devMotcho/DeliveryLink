# DeliveryLink

## Run with docker

``` bash
docker compose up --build -d
docker compose ps
docker compose logs -f web
```

## Create a superuser

``` bash
docker compose exec web python manage.py createsuperuser
```

## Start new app

``` bash
docker compose exec web python manage.py startapp <app_name>
```
