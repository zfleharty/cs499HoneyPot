FROM ubuntu:latest
MAINTAINER john snow

RUN apt-get update
RUN apt-get install -y build-essential gcc python
RUN apt-get install -y wget \
	farpd \
	libevent-1.4-2 \
	libpcap-dev \
	libdnet \
	libevent-dev \
	libdumbnet-dev \
	libpcre3-dev \
	libedit-dev \
	bison \
	flex \
	libtool \
	zlib1g-dev \
	automake
RUN apt-get upgrade -y
COPY ./honeyd/Honeyd/ /home/Honeyd/
WORKDIR /home/Honeyd/
RUN ./autogen.sh && ./configure && make && make install
WORKDIR /home
COPY ./honeyd.conf ./

farpd 192.168.1.77 -i eth0




