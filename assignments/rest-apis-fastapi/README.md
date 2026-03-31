# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework in Python, learning how to define routes, handle HTTP methods, work with request/response models, and test your API using FastAPI's built-in interactive documentation.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Create a FastAPI application with a basic project structure. Define a root endpoint that returns a welcome message and confirm the app runs correctly with Uvicorn.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Define a `GET /` route that returns a JSON welcome message (e.g., `{"message": "Welcome to my API"}`)
- Run the app using `uvicorn` and confirm it responds at `http://127.0.0.1:8000`


### 🛠️ Create a CRUD API for a Resource

#### Description
Implement a simple in-memory CRUD (Create, Read, Update, Delete) API for a resource of your choice (e.g., books, tasks, students). Use a Python list or dictionary to store the data.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource with at least 3 fields (e.g., `id`, `title`, `description`)
- Implement `GET /items` to return all items
- Implement `POST /items` to add a new item
- Implement `GET /items/{item_id}` to retrieve a single item by ID
- Implement `PUT /items/{item_id}` to update an existing item
- Implement `DELETE /items/{item_id}` to remove an item by ID
- Return appropriate HTTP status codes (e.g., `404` when an item is not found)
