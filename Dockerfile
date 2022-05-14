FROM python:3.8-alpine3.12

LABEL mantainer="Hugo Silva Álvarez <hugofer93@gmail.com>"

    # Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # Poetry
    POETRY_VERSION=1.1.13 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=1
    # Add Poetry bin to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /opt/plerk

RUN apk add --no-cache gcc g++ linux-headers postgresql-dev \
    && wget -qO- https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY . .

RUN poetry install --no-dev --no-root
