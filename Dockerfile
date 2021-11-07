# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM python:3.8.5

ENV APP_HOME=/code
# создать директорию /code
RUN mkdir $APP_HOME


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_HOME

RUN mkdir $APP_HOME/staticfiles

# скопировать файл requirements.txt из директории, в которой лежит докерфайл, в директорию /code
COPY requirements.txt .

# выполнить команду (как в терминале, с тем же синтаксисом) для установки пакетов из requirements.txt
RUN pip install -r /code/requirements.txt


# скопировать всё содержимое директории, в которой лежит докерфайл, в директорию /code
COPY . .

# при старте контейнера выполнить runserver
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

