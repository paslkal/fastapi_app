from fastapi import FastAPI
import json

with open('products.json') as f:
    products = json.load(f)

app = FastAPI()


@app.get("/products")
async def root():
    return products

@app.post('/products')
async def add_product():
    return 'add product'

@app.put('/products')
async def update_product():
    return 'update product'

@app.delete('/products')
async def delete_product():
    return 'delete product' 