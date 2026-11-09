# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to learn how HTTP methods, request validation, and CRUD operations work together to manage data.

## 📝 Tasks

### 🛠️	Create the API and Read Routes

#### Description
Complete the starter application so it serves a welcome message and a list of books. Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the server with `uvicorn main:app --reload`. Open `http://127.0.0.1:8000/docs` to try the routes.

#### Requirements
Completed program should:

- Create a FastAPI application
- Return a welcome message from `GET /`
- Return all sample books from `GET /books`


### 🛠️	Add Book Creation and Lookup

#### Description
Use the provided Pydantic `Book` model to accept new book details. Add routes that create a book and retrieve one book by its ID.

#### Requirements
Completed program should:

- Add `POST /books` to accept a book with a title and author, assign it a unique ID, and return the created book
- Add `GET /books/{book_id}` to return the matching book
- Return an HTTP 404 error when the requested book ID does not exist


### 🛠️	Update and Delete Books

#### Description
Complete the remaining routes so a client can update or remove a book by ID.

#### Requirements
Completed program should:

- Add `PUT /books/{book_id}` to replace a book's title and author
- Add `DELETE /books/{book_id}` to remove a book
- Return an HTTP 404 error when trying to update or delete a book that does not exist
