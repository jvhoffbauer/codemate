- This function is a GET request for an item with a specific ID using FastAPI's decorator `@app.get`.
- The path parameter `item_id` is validated using Pydantic's `Path()` class, which ensures it is greater than zero and less than or equal to 1000.
- An optional query parameter `q` can be passed in as well, which will also be included in the response dictionary.