from fastapi import FastAPI, Request
from connection.database import database
from connection.models import Books
from schemas.input import Book 
import uvicorn 

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def index():
    return {"message": "hello world"}

@app.get("/books/")
async def get_all_books():
    query = Books.select()
    return await database.fetch_all(query)

@app.post("/books/")
async def create_book(request:Request):
    data = await request.json()
    query = Books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info", reload=True, debug=False)