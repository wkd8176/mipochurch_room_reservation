# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set enviroment variales
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

COPY . /usr/src/app/

# install dependencies 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt