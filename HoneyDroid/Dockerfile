FROM ubuntu:trusty
MAINTAINER john snow

RUN apt-get update
RUN apt-get install -y build-essential gcc
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
COPY ./honeyd /home
WORKDIR /home/honeyd/Honeyd
RUN ./autogen.sh && ./configure && make && make install



