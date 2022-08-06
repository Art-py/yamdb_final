## Описание
Бэкенд проекта YaMDb.
"Запакованный" в docker-compose.

![workflow](https://github.com/Danstiv/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект собирает отзывы пользователей на произведения. API позволяет создавать, редактировать, удалять отзывы, а также ставить произведению оценку.

## Использованные технологии
- django 2
- django rest framework
- python 3
- Docker

## Как запустить проект
Собрать и запустить контейнеры командой из директории с файлом "docker-compose.yaml":

```
docker-compose up -d --build
```
Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```
Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```
Собрать статику:
```
docker-compose exec web python manage.py collectstatic
```

При необходимости заполнить базу тестовыми данными (из приложенных файлов .csv):

```
docker-compose exec web python manage.py filldb
```

При необходимости заполнить базу тестовыми данными (из файла фикстуры):

```
docker-compose exec web python manage.py loaddata fixtures.json
```

## документация API

Документация API доступна по адресу http://127.0.0.1:8000/redoc/

### Примеры работы с API
 
#### Регистрация пользователей

1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
2. **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес `email`.
3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле.

## Авторы проекта

- Жуков Артем - [Art-py](https://github.com/Art-py)
- Пылаев Данил - [Danstiv](https://github.com/danstiv)
- Воронюк Ольга - [Helga61](https://github.com/Helga61)
- Тростянский Дмитрий - [trdeman](https://github.com/trdeman)
