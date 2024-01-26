- Defines a GET request endpoint at `/text`.
- Returns a string response with the text "Hello World".

2) Given the following source code, what is the purpose of the `@app.post()` decorator and how should I structure my request body to use this endpoint? Answer according to: This function handles POST requests for /items.

```python
from fastapi import FastAPI, Body

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items", response_model=Item)
async def create_item(item: Item = Body(...)):
    #...
```

Purpose of `@app.post()` decorator:
- Marks the function as an endpoint for handling HTTP POST requests.
- Specifies that the endpoint is located at the URL path `/items`.

Structure of request body:
- The request body must be in JSON format and conform to the schema defined by the `Item` model class (which has fields named `name`, `description`, `price`, and `tax`).
- The `Body` parameter decorator ensures that the request body is automatically parsed into a Python object of type `Item` before being passed to the function as its argument.
- If any required fields are missing from the request body, FastAPI will raise a validation error.