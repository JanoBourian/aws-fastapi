from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/hello/{name}")
async def say_hello(name:str = None):
    return {"message": f"Hello {name}"}