from fastapi import FastAPI
from database.database import db
from database.models import Test

app = FastAPI()

@app.get("/")
async def root():
    items = db.query(Test).all()
    print(f"Items {items}")
    return {"message": "Hello"}

@app.get("/hello/{name}")
async def say_hello(name:str = None):
    return {"message": f"Hello {name}"}