from sqlalchemy import Column, String, Float, Integer
from database import Base

class itemmodel(Base):
    __tablename__ = "items"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)

    