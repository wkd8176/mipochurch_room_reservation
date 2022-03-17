# pull official base image
FROM python:latest

# set work directory
WORKDIR /usr/src/app

# set enviroment variales
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY . /usr/src/app/

# install dependencies 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt