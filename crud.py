from sqlalchemy.orm import Session

import models

def find_product(db: Session, *, id: int):
    product = db.query(models.Product).filter_by(id = id).first()

    return product

def get_products(
    db: Session, 
    *, 
    skip: int = 0, 
    limit:int = 100, 
    price: int = 0, 
    reverse: bool = False
):
    if (price):
        if (reverse):
            return (
                db.query(models.Product)
                    .filter(models.Product.price_cents < price)
                    .offset(skip)
                    .limit(limit)
                    .all()
            )


        return (
            db.query(models.Product)
                .filter(models.Product.price_cents >= price)
                .offset(skip)
                .limit(limit)
                .all()
        )

    
    return db.query(models.Product).offset(skip).limit(limit).all()

def add_product(db: Session, product):
    new_product = models.Product(**product.model_dump()) 

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product

def update_price(db: Session, *, id: int, product):
    db.query(models.Product).\
        filter_by(id = id).\
        update({"price_cents": product.price_cents})
    
    db.commit()
    print(product.price_cents)

    return {"message":'Product has been updated'}

def delete_product(db: Session, *, id: int):
    db.query(models.Product).filter_by(id = id).delete()

    db.commit()

    return {"message": 'Product has been deleted'}


def get_categories(db: Session, *, id: int):
    product = find_product(db, id=id)

    categories = product.categories

    return categories