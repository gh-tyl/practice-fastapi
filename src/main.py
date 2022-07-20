from fastapi import FastAPI
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
def main_aialgo8(sentence: Sentence):
    print(f"sentence: {sentence}")
    sentence = sentence["sentence"]
    words = aialgo8.words_genkei(sentence)
    print(f"words: {words}")
    return words
