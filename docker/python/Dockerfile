FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

ARG LOG_FILE

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.2 \
    LOG_FILE=$LOG_FILE

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev libffi-dev linux-headers musl-dev zlib zlib-dev

RUN pip install poetry==$POETRY_VERSION

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --only=main --no-root

COPY . .

RUN touch $LOG_FILE

CMD ["python3", "main.py"]