from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import json
import crud
import schemas
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

with open('products.json') as f:
    products = json.load(f)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def get_products(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.post('/products', response_model=schemas.Product)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.add_product(db, product=product)

@app.put('/products')
def update_product():
    return 'update product'

@app.delete('/products')
def delete_product():
    return 'delete product' 