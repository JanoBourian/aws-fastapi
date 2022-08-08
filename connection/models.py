from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from .database import database, database_url
from sqlalchemy.orm import relationship
import sqlalchemy

meta = MetaData()

Books = Table(
    "books",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("author", String, nullable=False),
    Column("pages", Integer, nullable=False),
)

Readers = Table(
    "readers",
    meta,
    Column("id", Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
)

Readers_Books = Table(
    "readers_books",
    meta,
    Column("id", Integer, primary_key=True),
    Column("book_id", ForeignKey("books.id"), nullable=False, index=True),
    Column("reader_id", ForeignKey("readers.id"), nullable=False, index=True),
)

engine = sqlalchemy.create_engine(database_url)
meta.create_all(engine)
