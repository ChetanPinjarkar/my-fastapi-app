from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, CI/CD World!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}
