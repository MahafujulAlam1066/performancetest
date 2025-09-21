import pytest
from fastapi.testclient import TestClient
from sourcecode.performance_test import api 
client = TestClient(api)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

def test_get_books_initially_empty():
    response = client.get("/book")
    assert response.status_code == 200
    assert response.json() == []

def test_add_book():
    book_data = {
        "id": 1,
        "name": "Python 101",
        "description": "Learn Python programming",
        "isAvailable": True
    }
    response = client.post("/book", json=book_data)
    assert response.status_code == 200
    assert response.json() == [book_data]

def test_update_book():
    updated_book_data = {
        "id": 1,
        "name": "Python 101 Updated",
        "description": "Learn Python programming - Updated",
        "isAvailable": False
    }
    response = client.put("/book/1", json=updated_book_data)
    assert response.status_code == 200
    assert response.json() == updated_book_data

def test_update_nonexistent_book():
    updated_book_data = {
        "id": 99,
        "name": "Nonexistent Book",
        "description": "This book does not exist",
        "isAvailable": False
    }
    response = client.put("/book/99", json=updated_book_data)
    assert response.status_code == 200
    assert response.json() == {"error": "Book Not Found"}

def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_delete_nonexistent_book():
    response = client.delete("/book/99")
    assert response.status_code == 200
    assert response.json() == {"error": "Book not found, deletion failed"}
