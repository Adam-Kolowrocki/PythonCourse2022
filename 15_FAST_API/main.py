from fastapi import FastAPI

from pydantic import BaseModell

app = FastAPI()
app.counter = 0


class HelloResponse(BaseModell):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World - now I'm on local server..."}


@app.get('/counter')
def counter():
    app.counter += 1
    return f'Wejść na stronę było dokładnie: {str(app.counter)}'


@app.get("/hello/{name}", response_model=HelloResponse)
def hello_name_view(name: str):
    return HelloResponse(msg= f'Hello {name}!')
