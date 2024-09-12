from fastapi import FastAPI, Depends, HTTPException
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


@app.get("/products", response_model=list[schemas.Product])
def get_products(
    price: int=0,
    reverse: bool = False, 
    skip: int=0, 
    limit: int=100, 
    db: Session = Depends(get_db)
):
    return crud.get_products(
        db, 
        skip=skip, 
        limit=limit, 
        price=price, 
        reverse=reverse
    )


@app.post('/products', response_model=schemas.Product, status_code=201)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.add_product(db, product=product)


@app.put('/products/{id}')
def update_product(
    id: int, 
    product: schemas.ProductUpdate, 
    db: Session = Depends(get_db)
):
    found_product = crud.find_product(db, id=id)

    if (not found_product):
        return HTTPException(status_code=404, detail='Product not found')


    return crud.update_price(db, id=id, product=product)


@app.delete('/products/{id}', response_model=schemas.ProductMessage)
def delete_product(id: int, db: Session = Depends(get_db)):
    found_product = crud.find_product(db, id=id)

    if (not found_product):
        return HTTPException(status_code=404, detail='Product not found')

    return crud.delete_product(db, id=id) 


@app.get('/products/categories/{id}', response_model=schemas.ProductCategories)
def get_categories(id: int, db: Session = Depends(get_db)):
    found_product = crud.find_product(db, id=id)

    if (not found_product):
        return HTTPException(status_code=404, detail='Product not found')

    return crud.get_categories(db, id=id)