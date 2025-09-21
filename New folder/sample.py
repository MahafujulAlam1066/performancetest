from fastapi.testclient import TestClient
from bookstore_api import api  # import your FastAPI instance here

client = TestClient(api)

# Test home endpoint (GET /book)
def test_home():
    response = client.get("/book")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my shop"}

# Test POST /book - create new book
def test_post_book():
    response = client.post("/book", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "price": 15,
        "in_stock": True
    })
    assert response.status_code == 200
    books = response.json()
    assert any(book["title"] == "1984" for book in books)

# Test GET /book/{book_id} - get specific book
def test_get_book():
    response = client.get("/book/1")
    assert response.status_code == 200
    book = response.json()
    assert book["id"] == 1
    assert book["title"] == "1984"

# Test PUT /book/{book_id} - update book details
def test_update_book():
    response = client.put("/book/1", json={
        "id": 1,
        "title": "1984 (Updated)",
        "author": "George Orwell",
        "price": 20,
        "in_stock": False
    })
    assert response.status_code == 200
    books = response.json()
    updated_book = next((b for b in books if b["id"] == 1), None)
    assert updated_book is not None
    assert updated_book["title"] == "1984 (Updated)"
    assert updated_book["price"] == 20
    assert updated_book["in_stock"] is False

# Test DELETE /book/{book_id} - delete book
def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    books = response.json()
    assert all(book["id"] != 1 for book in books)
