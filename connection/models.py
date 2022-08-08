from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from .database import database, database_url
from sqlalchemy.orm import relationship
import sqlalchemy

meta = MetaData()

Books = Table(
    'books', meta, 
    Column("id", Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False)
)

engine = sqlalchemy.create_engine(database_url)
meta.create_all(engine)