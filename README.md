# api_YamDB

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.
Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти).
Из множества оценок автоматически высчитывается средняя оценка произведения.

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека djoser - активация аккаунтов с помощью почты
- библиотека django-filter - фильтрация запросов
- базы данны - SQLite3 и PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- система управления версиями - git

## Как запустить проект без использования Docker (база данных SQLite3):

1) Клонируйте репозитроий с проектом:
```
git clone 
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3) Создайте в директории файл .env и поместите туда SECRET_KEY, необходимый для запуска проекта
   - сгенерировать ключ можно на сайте [Djecrety](https://djecrety.ir/)

4) Выполните миграции:
```
python manage.py migrate
```
5) Cоздайте суперпользователя:
```
python manage.py createsuperuser
```
6) Загрузите тестовые данные:
```
python manage.py loaddata fixtures.json
```
8) Запустите сервер:
```
python manage.py runserver
```
__________________________________
С помощью команды pytest вы можете запустить тесты и проверить работу модулей:
```
pytest
```

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация доступна по адресу http://127.0.0.1:8000/redoc/

## Как запустить проект, используя Docker (база данных PostgreSQL):
1) Клонируйте репозитроий с проектом:
```
git clone 
```
2) В директории проекта создайте файл .env, в котором пропишите следующие переменные окружения (для тестирования можете использовать указанные значения переменных):
 - SECRET_KEY=p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs
 - EMAIL_HOST_USER= # почта для отправки писем пользователям
 - EMAIL_HOST_PASSWORD= # пароль от почты 
 - DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
 - DB_NAME=postgres # имя базы данных
 - POSTGRES_USER=postgres # логин для подключения к базе данных
 - POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
 - DB_HOST=db # название сервиса (контейнера)
 - DB_PORT=5432 # порт для подключения к БД

3) С помощью Dockerfile и docker-compose.yaml разверните проект:
```
docker-compose up --build
```
4) В новом окне терминала узнайте id контейнера api_yamdb_web и войдите в контейнер:
```
docker container ls
```
```
docker exec -it <CONTAINER_ID> bash
```
5) В контейнере выполните миграции, создайте суперпользователя и заполните базу начальными данными:
```
python manage.py migrate

python manage.py createsuperuser

python manage.py loaddata fixtures.json
```
_________________________________
Ваш проект запустился на http://0.0.0.0:8000/

Полная документация доступна по адресу http://127.0.0.1:8000/redoc/

Вы можете запустить тесты и проверить работу модулей:
```
docker exec -ti <container_id> pytest
```

## Алгоритм регистрации пользователей
1) Пользователь отправляет запрос с параметрами *email* *username* и *password* по адресу:
    ```
     http://127.0.0.1:8000/api/v1/auth/users/
    ```
2) YaMDB отправляет письмо с url на адрес *email* .
   ```
   http://127.0.0.1:8000/#/activate/MTA1/avo2d8-a224300ccb8c59cb0ab77e7d2d0e74fe
   
   uid = MTA1
   token = avo2d8-a224300ccb8c59cb0ab77e7d2d0e74fe
   ```
3) Нужно отправить *uid* и *token* на url и подтвердить свой аккаунт
   ```
   http://127.0.0.1:8000/api/v1/auth/users/activate/
   ```
4) Пользователь отправляет запрос с параметрами *email* *username* и *password* на url, в ответе на запрос ему приходит token (JWT-токен).
   ```
   http://127.0.0.1:8000/api/v1/auth/token/login/
   ```

## Ресурсы API YaMDb

- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.