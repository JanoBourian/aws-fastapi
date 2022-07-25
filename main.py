from fastapi import FastAPI
from connection.database import database
from connection.models import Test, Books

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/books/")
async def get_all_books():
    query = Books.select()
    return await database.fetch_all(query)