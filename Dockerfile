FROM python:3.7-alpine3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps zlib-dev jpeg-dev gcc musl-dev postgresql-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && adduser -D processuser

# Add docker-compose-wait tool
# https://www.datanovia.com/en/lessons/docker-compose-wait-for-container-using-wait-tool/docker-compose-wait-for-postgres-container-to-be-ready/
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

USER processuser
