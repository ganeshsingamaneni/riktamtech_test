FROM ubuntu:18.04

FROM python:3.6
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get -y install cmake protobuf-compiler
RUN apt-get install libmysqlclient-dev
RUN apt-get install -y git

RUN cd ..


COPY ./requirements.txt /app/requirements.txt 

WORKDIR /app

# Copy the current directory contents into the container /app where . is the relative directory AKA flask
ADD . /app

RUN pip3 install -r requirements.txt 

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]


