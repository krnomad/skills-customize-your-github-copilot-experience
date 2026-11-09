from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


@app.get("/books")
def list_books():
    # TODO: Return the list of books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return a book, or raise an HTTP 404 error.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Assign a unique ID, save the new book, and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # TODO: Update the matching book, or raise an HTTP 404 error.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the matching book, or raise an HTTP 404 error.
    pass
