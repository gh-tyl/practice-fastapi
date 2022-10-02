import copy
import os
from base64 import b64decode, b64encode

from fastapi import FastAPI
from genericpath import isdir
from starlette.middleware.cors import CORSMiddleware

import aialgo8

app = FastAPI()

# CORSを回避
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return {"Hello": "World"}


# 受け取るデータの型を定義
class Sentence(dict):
    sentence: str


@app.post("/aialgo8/")
def main(sentence: Sentence):
    print(f"sentence: {sentence}")
    sentence = sentence["sentence"]
    words = aialgo8.words_genkei(sentence)
    print(f"words: {words}")
    return words


class Filedata(dict):
    filename = ""
    data = bytes


@app.post("/aialgo3/")
def main(filedata: Filedata):
    print(f"filedata: {filedata}")
    filename = filedata["filename"]
    data: str = str(filedata["data"])
    print(f"data: {data}")
    print(f"data_type: {type(data)}")
    data = bytes(data, encoding="utf-8")
    print(f"data: {data}")
    print(f"data_type: {type(data)}")
    data_dir: str = "data"
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, filename), "wb") as f:
        f.write(b64decode(data))
    return True


@app.get("/aialgo7/")
def main():
    filepath: str = "./data/sample_metadata.csv"
    # 1行ずつ読み込み
    csv_data = open(filepath, "r").readlines()
    # 二重配列に変換
    csv_data_ = [d.split(",") for d in csv_data]
    # 値をnuxtへ
    data = {"statusCode": 200, "body": {"csv_data": csv_data_}}
    return data
