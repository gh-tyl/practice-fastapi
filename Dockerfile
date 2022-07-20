FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y \
    git \
    curl \
    sudo \
    wget \
    locales \
    python3.8 \
    python3-pip \
    libgl1-mesa-dev \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8

RUN echo "ja_JP UTF-8" > /etc/locale.gen
RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
    cd mecab-ipadic-neologd && \
    sudo bin/install-mecab-ipadic-neologd -n -y && \
    echo "dicdir=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd">/etc/mecabrc && \
    cp /etc/mecabrc /usr/local/etc/

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
    pip3 install --upgrade pip setuptools wheel && \
    pip3 install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "${HOST}", "--port", "${PORT}", "--reload"]
