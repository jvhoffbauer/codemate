- Defines a GET request for `http://localhost:8000/items/`.
- Accepts an optional query parameter named `hidden_query`, which is marked as not being included in the schema using FastAPI's `Query()` decorator with the `include_in_schema` argument set to False.
- If the `hidden_query` parameter is provided, returns it directly; otherwise, returns a default value of "Not found".