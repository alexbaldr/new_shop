FROM python:3.8-alpine

ENV PYTHONDONTWRUTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update &&\
 apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY entrypoint.sh .

COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]