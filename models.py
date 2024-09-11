from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(JSON)
    price_cents = Column(Integer)
    keywords = Column(JSON)