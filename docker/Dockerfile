FROM python:3.9.17-slim

WORKDIR /usr/src

RUN pip install --upgrade pip

COPY ./file/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get -y update && apt -y install wget && apt install unzip && apt -y install curl

#2023-09-07, chrome ver.116 & chromedriver ver.116
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip


WORKDIR /tmp
RUN unzip chromedriver.zip
RUN mv /tmp/chromedriver-linux64/chromedriver  /usr/bin/


#Network
RUN apt-get update && apt-get install net-tools && apt-get install -y iproute2 && apt-get install -y iputils-ping && apt-get install -y curl && apt-get install -y vim


RUN mkdir /test
WORKDIR /test
COPY ./file/selenium.test.py  ./

CMD [ "python", "./selenium.test.py" ]
