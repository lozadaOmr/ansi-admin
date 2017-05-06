FROM python:2.7
MAINTAINER Omar Lozada <omar.lozada@infoshiftinc.com>

RUN apt-get update
RUN apt-get install python-mysqldb
RUN apt-get -y autoremove

RUN mkdir /opt/app
VOLUME /opt/app
WORKDIR /opt/app
ADD ./src/requirements.txt .

RUN pip install -r requirements.txt
