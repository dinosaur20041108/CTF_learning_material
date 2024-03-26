
FROM ubuntu:16.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    echo 'ctf - nproc 1500' >>/etc/security/limits.conf && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf

RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail


COPY ./pwn /home/ctf/
COPY ./flag.sh /flag.sh
RUN chown root:root /flag.sh
RUN chmod +x  /flag.sh
ENV DASFLAG=flag{flag_test}

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf 

CMD exec /bin/bash -c "/etc/init.d/xinetd start; /flag.sh ; trap : TERM INT; sleep infinity & wait"

EXPOSE 9999
