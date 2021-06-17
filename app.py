from fastapi import FastAPI

app = FastAPI()


@app.get("/hello-world")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/hello-name")
async def hello_name(name: str):
    return {"message": "Hello "+ name}
