from fastapi.testclient import TestClient
from bookstore_api import api

client = TestClient(api)

def test_home():
    response = client.get("/book")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my shop"}

def test_post_book():
    book_data = {
        "id": 1,
        "title": "1990",
        "author": "Sayem",
        "price": 155,
        "in_stock": True
    }
    response = client.post("/book", json=book_data)
    assert response.status_code == 200
    assert response.json() == [book_data]  # List of books
    
