# plerk-api

This is a REST API with [Django](https://docs.djangoproject.com/en/3.2/), [Django REST Framework](https://www.django-rest-framework.org/), [RabbitMQ](https://www.rabbitmq.com/) and [Redis](https://redis.io/)


## Overview: PLERK API

[Problem Statement](PROBLEM-STATEMENT.md) proposed by [PLERK](https://www.plerk.io/)


## Table of Contents

* [Overview](#plerk-api)
* [Main Dependencies](#Main-Dependencies)
* [Project Configuration](#Project-Configuration)


## Main Dependencies

    Python              ~3.8
    Django              ~3.2
    djangorestframework ~3.13
    PostgreSQL          ~12.7
    RabbitMQ            ~3.8
    Redis               ~7.0

For more details, see the [pyproject.toml file](pyproject.toml).

## Docker Configuration

- [Install Docker](https://docs.docker.com/engine/install/)

- [Install Docker Compose](https://docs.docker.com/compose/install/#install-compose)

## Project Configuration

- Clone this [repository](https://github.com/hugofer93/plerk-api):

        git clone https://github.com/hugofer93/plerk-api.git

- Create `.env` file based on `.env.sample`:

        cp .env.sample .env

    **Production or Staging Environment**:

    - Set `DEBUG=false`

    **Develop Environment**:

    - Set `DEBUG=true`

- Up Services with docker-compose:

    **Production or Staging Environment**:

        docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

    **Develop Environment**:

        docker-compose up -d

- Execute commands in container (e.g.):

        docker-compose exec api poetry run python manage.py shell

- Load test database (csv file):

        docker-compose exec api poetry run python utility/load_csv_to_database.py

- Create an Admin User for the project:

        docker-compose exec api poetry run python manage.py createsuperuser

- Show containers logs:

    For Django Project:

        docker-compose logs -f api

    For Celery (*SHOW CELERY BEAT TOO, ONLY IN DEV ENVIRONMENT*):

        docker-compose logs -f celery

    For Celery Beat (*ONLY FOR PROD ENVIRONMENT*):

        docker-compose logs -f celerybeat
