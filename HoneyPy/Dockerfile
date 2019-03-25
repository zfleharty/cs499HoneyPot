# auto-generated Dockerfile
FROM alpine
MAINTAINER foospidy
RUN apk update && \
    apk add wget unzip ca-certificates python py-twisted py-pip py-setuptools python-dev musl-dev gcc && \
    update-ca-certificates && \
    pip install --upgrade pip && \
    pip install requests && \
    pip install pipreqs && \
    pip install dnslib && \
    pip install mysql.connector && \
    rm -rf /var/cache/apk/*
RUN addgroup honey && \
    adduser -s /bin/bash -D -G honey honey
RUN mkdir -p /opt && \
    cd /opt && wget https://github.com/foospidy/HoneyPy/archive/master.zip && \
    cd /opt && unzip master.zip && \
    cd /opt && mv HoneyPy-master HoneyPy && \
    cd /opt && rm master.zip && \
    chmod +x /opt/HoneyPy/Honey.py
COPY etc/honeypy.cfg /opt/HoneyPy/etc/
COPY etc/services.cfg /opt/HoneyPy/etc/
COPY loggers /opt/HoneyPy/loggers
RUN pipreqs --force /opt/HoneyPy && \
    chown -R honey:honey /opt/HoneyPy
RUN cd /opt && wget https://github.com/foospidy/clilib/archive/master.zip && \
    cd /opt && unzip master.zip && \
    cd /opt && rm master.zip && \
    cd /opt && mv clilib-master clilib && \
    cd /opt/clilib && python setup.py bdist_egg && \
    cd /opt/clilib && easy_install-2.7 -Z dist/clilib-0.0.1-py2.7.egg
RUN cd /opt && wget https://github.com/foospidy/ipt-kit/archive/master.zip && \
    cd /opt && unzip master.zip && \
    cd /opt && rm master.zip && \
    cd /opt && mv ipt-kit-master ipt-kit
USER honey
WORKDIR /opt/HoneyPy
EXPOSE 7/tcp
EXPOSE 8/tcp
EXPOSE 23/tcp
EXPOSE 24/tcp
EXPOSE 2048/tcp
EXPOSE 4096/tcp
EXPOSE 9200/tcp
EXPOSE 7/udp
EXPOSE 8/udp