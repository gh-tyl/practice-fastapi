FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y \
    python3.8 \
    python3-pip \
    libgl1-mesa-dev
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
    pip3 install --upgrade pip setuptools wheel && \
    pip3 install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "${HOST}", "--port", "${PORT}", "--reload"]
