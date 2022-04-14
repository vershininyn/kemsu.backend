FROM ubuntu:latest
MAINTAINER vyn "vershininyn@yandex.ru"

RUN apt-get update -y && apt-get -y install sudo
RUN useradd -m kemsu_flask && echo "kemsu_flask:kemsu_flask" | chpasswd && adduser kemsu_flask sudo

WORKDIR /home/kemsu_flask
COPY ./requirements.txt ./requirements.txt

RUN apt-get install -y python3-pip python3-dev && apt-get install -y python3.8-venv
RUN python3 -m venv ./venv
RUN ./venv/bin/pip install -r requirements.txt

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y nginx

RUN mkdir /etc/nginx/logs
RUN rm -f /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/
COPY ./proxy.conf /etc/nginx/

COPY backend.py boot.sh ./
COPY ./templates ./templates

RUN chmod +x boot.sh

ENV FLASK_APP ./backend.py

RUN chown -R kemsu_flask:kemsu_flask ./
USER kemsu_flask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]