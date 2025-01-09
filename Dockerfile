FROM python:3.12.0-slim

ARG APP_USER=backend_assesment

ARG APP_HOME=/app

RUN adduser --disabled-password --gecos '' ${APP_USER}
RUN adduser ${APP_USER} sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV PYTHONUNBUFFERED 1

RUN apt update \
  && apt install -y libpq-dev gcc

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR ${APP_HOME}

COPY pyproject.toml ${APP_HOME}
COPY poetry.lock ${APP_HOME}
RUN poetry config virtualenvs.create false && poetry install --only main

COPY . ${APP_HOME}

EXPOSE 80

RUN chmod ugo+rwx -R /app

CMD /bin/sh -c "python manage.py migrate --noinput; \
                python manage.py collectstatic --noinput; \
                gunicorn --config /app/src/gunicorn_conf.py src.config.wsgi:application"
