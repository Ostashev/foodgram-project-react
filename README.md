# praktikum_new_diplom
адрес сервера: https://spisok.ddns.net
логин админа: admin
пароль админа: admin

# Описание:
Foodgram - это сервис для публикаций и обмена рецептами. Пользователи могут подписываться на понравившихся авторов, добавлять рецепты в избранное, в покупки, скачивать список покупок.

# Стек технологий:
Python 3.9.5, Django 4.2.1, Django REST Framework 3.14.0, PostgresQL, Docker, Yandex.Cloud.

# Установка:
## Для запуска локально, создайте файл .env в главной директории с содержанием:
```
DEBUG=FALSE
SECRET_KEY=...
ALLOWED_HOSTS=localhost 127.0.0.1 ... ...

POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
DB_NAME=foodgram
```
## Установка Docker:
Для запуска проекта вам потребуется установить Docker и docker-compose.

Для установки на linux выполните следующие команды:
```
sudo apt install docker docker-compose
```

## Запуск проекта:
Запустите docker-compose-local из дерриктории infra/:
```
sudo docker compose -f docker-compose-local.yml up
```
Выполните миграции:
```
sudo docker compose -f docker-compose-local.yml exec backend python manage.py migrate
```
Соберите статику и копируйте ее:
```
sudo docker compose -f docker-compose-local.yml exec backend python manage.py collectstatic
```
```
sudo docker compose -f docker-compose-local.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```
Загрузите ингредиенты:
```
sudo docker compose -f docker-compose-local.yml exec backend python manage.py load_ingredients
```