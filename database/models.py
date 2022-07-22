from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Test(Base):
    __tablename__ = 'test'
    id_test = Column(Integer, primary_key=True, index=True)
    testname = Column(String, unique=True, nullable=False)