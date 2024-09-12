from fastapi.testclient import TestClient
import schemas
from main import app

client = TestClient(app)

# def setup_function():
#     pass


# def test_get_products():
#     pass


def test_add_product():
    product =   {
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

# def test_update_product():
#     pass


# def test_delete_product():
#     pass
