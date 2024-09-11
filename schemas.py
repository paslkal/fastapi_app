from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    rating: dict
    price_cents: int
    categories: list[str] 


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: str | None = None
    rating: dict | None = None
    price_cents: int
    categories: list[str] | None = None
