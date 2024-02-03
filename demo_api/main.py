import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return dict(hello="world")


@app.get("/contents")
def contents():
    with open("../content_target_output.json", "r") as content:
        contents = json.loads(content.read())
    return contents


@app.get("/authors")
def authors():
    with open("../author_target_output.json", "r") as author:
        authors = json.loads(author.read())
    return authors
