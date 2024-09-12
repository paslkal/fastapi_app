from fastapi.testclient import TestClient
import schemas
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get('/products')

    assert response.status_code == 200
    assert response.json() == []


def test_add_product():
    product = {
        "name": "Women's Chiffon Beachwear Cover Up - Black",
        "rating": {
        "stars": 4.5,
        "count": 235
        },
        "price_cents": 2070,
        "categories": [
            "robe",
            "swimsuit",
            "swimming",
            "bathing",
            "apparel"
        ]
    }

    response = client.post('/products', json=product)

    assert response.status_code == 201
    assert response.json() == dict(id=1, **product)

def test_update_product():
    id = 1

    response = client.put(f'/products/{id}', json={"price_cents": 1030})

    assert response.status_code == 200
    assert response.json() == {"message": "Product has been updated"}


def test_delete_product():
    id = 1

    response = client.delete(f'/products/{id}')

    assert response.status_code == 200
    assert response.json() == {"message": "Product has been deleted"}

