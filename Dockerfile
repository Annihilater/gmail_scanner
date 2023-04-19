FROM python:3.9

ENV PATH /usr/local/bin:$PATH

WORKDIR /opt/apps/gmail_scanner

# debain 换中科大源
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list
RUN apt-get update && \
    apt-get install apt-file -y && \
    apt-file update && \
    apt-get install vim -y

COPY requirements.txt .
# PIP换源: 阿里源、中科大源、豆瓣源、清华源
ARG PIP_INDEX_ALIYUN="-i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com"
ARG PIP_INDEX_USTC="-i https://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn"
ARG PIP_INDEX_DOUBAN="-i https://pypi.douban.com/simple/ --trusted-host pypi.douban.com"
ARG PIP_INDEX_TSINGHUA="-i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn"
RUN pip3 install -r requirements.txt ${PIP_INDEX_USTC}

COPY . .
