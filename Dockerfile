FROM python:3.4

MAINTAINER Vasja Volin vasja.volin@gmail.com

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
