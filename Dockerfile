FROM python:3.9-slim

ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir poetry; poetry install --without test --no-root
EXPOSE 8000
CMD ./run.sh
