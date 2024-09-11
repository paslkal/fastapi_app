from sqlalchemy.orm import Session
from fastapi import Depends

import models

def get_products(db: Session, skip: int = 0, limit:int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def add_product(db: Session, product):
    new_product = models.Product(
        name=product.name, 
        rating=product.rating,
        price_cents=product.price_cents,
        keywords=product.keywords
    ) 

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product():
    pass

def delete_product():
    pass
