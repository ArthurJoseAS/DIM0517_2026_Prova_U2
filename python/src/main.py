from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, dude!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}
