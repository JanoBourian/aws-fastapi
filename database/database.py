from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from .config import init_connection_engine

engine = init_connection_engine()

Session = sessionmaker(autocommit = False, autoflush = True, bind = engine)

Base = declarative_base()

db = Session()