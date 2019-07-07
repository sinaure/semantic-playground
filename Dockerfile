FROM python:3.7.2-slim

ENV INSTALL_PATH /scripts
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

RUN apt update
RUN apt install -y python3-pip python3-dev libcurl4-gnutls-dev librtmp-dev git 
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD /bin/bash