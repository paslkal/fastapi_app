from sqlalchemy.orm import Session
from fastapi import Depends

import models

def get_products(db: Session, *, skip: int = 0, limit:int = 100):
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

def update_price(db: Session, *, id: int, product):
    db.query(models.Product).filter_by(id = id).update({"price_cents": product.price_cents})
    
    db.commit()

    return 'Product has been updated'

def delete_product(db: Session, *, id: int):
    db.query(models.Product).filter_by(id = id).delete()

    db.commit()

    return 'Product has been deleted'


def get_categories(db: Session, *, id: int):
    product = db.query(models.Product).filter_by(id = id).first()

    categories = product.keywords

    return categories