from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# TODO: Define your Pydantic model here
# Example:
# class Item(BaseModel):
#     id: int
#     title: str
#     description: str


# In-memory storage
items = []


@app.get("/")
def read_root():
    # TODO: Return a JSON welcome message
    pass


@app.get("/items")
def get_items():
    # TODO: Return all items
    pass


@app.post("/items", status_code=201)
def create_item(item):
    # TODO: Add a new item to the list and return it
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Find and return the item with the given ID
    # Raise HTTPException with status_code=404 if not found
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item):
    # TODO: Find the item and update its fields
    # Raise HTTPException with status_code=404 if not found
    pass


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # TODO: Remove the item with the given ID
    # Raise HTTPException with status_code=404 if not found
    pass
