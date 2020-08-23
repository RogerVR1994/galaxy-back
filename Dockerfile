FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3-pip -y 

WORKDIR /app/
ADD . /app/
RUN pip3 install -r requirements.txt
EXPOSE 8000