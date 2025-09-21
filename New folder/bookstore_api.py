from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: int
    in_stock: bool

books: List[Book] = []

api = FastAPI()

@api.get("/book")
def home():
    return {"message": "Welcome to my shop"}

@api.get("/book/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"message": "Book not found"}

@api.post("/book")
def post_book(book: Book):
    books.append(book)
    return books

@api.put("/book/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return books
    return {"message": "Error in updating"}

@api.delete("/book/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return books
    return {"message": "Error in deletion"}


