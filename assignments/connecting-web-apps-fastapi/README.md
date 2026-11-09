# 📘 Assignment: Connecting a Web App to FastAPI

## 🎯 Objective

Build a browser-based book catalog that uses JavaScript `fetch` to communicate with a FastAPI service. Practice displaying API data, submitting forms, and handling loading and error states.

## 📝 Tasks

### 🛠️ Configure Browser Access and Display Books

#### Description
First complete the [Building REST APIs with FastAPI](../building-rest-apis-fastapi/README.md) assignment. Add FastAPI's CORS middleware to that API so a page served from `http://localhost:5500` can send requests to it. Run the API from its assignment folder with `uvicorn main:app --reload`, then serve this starter page from this assignment folder with `python -m http.server 5500`. Open `http://localhost:5500/starter-code.html` in your browser.

#### Requirements
Completed program should:

- Allow requests from `http://localhost:5500` in the FastAPI CORS configuration
- Request and display the books from `GET /books`
- Show a useful message while books are loading or when the request fails


### 🛠️ Add Books from the Page

#### Description
Connect the book form to the API. Submit new book details without reloading the page, then refresh the displayed list.

#### Requirements
Completed program should:

- Require a non-empty title and author before sending a request
- Send a `POST /books` request with a JSON body containing the title and author
- Display the new book after it is created and show a useful message if the request fails


### 🛠️ Update and Remove Books

#### Description
Add controls to each book so users can change its title and author or remove it. Refresh the list after each successful change.

#### Requirements
Completed program should:

- Send a `PUT /books/{book_id}` request with the edited title and author
- Send a `DELETE /books/{book_id}` request to remove a book
- Handle failed requests without leaving the page in a misleading state