from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from .database import database, database_url
from sqlalchemy.orm import relationship
import sqlalchemy

meta = MetaData()

Test = Table(
    'test', meta, 
    Column('id_test', Integer, primary_key=True, index=True),
    Column('nametest', String, unique=True, nullable=False)
)

Books = Table(
    'books', meta, 
    Column("id", Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False)
)

engine = sqlalchemy.create_engine(database_url)
meta.create_all(engine)