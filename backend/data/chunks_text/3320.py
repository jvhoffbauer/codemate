- Creates a new instance of `FastAPI`.
- Defines a nested router with prefix "/nested".
- Registers an endpoint at "/nested/test" that accepts a query parameter named "var".
- Includes the defined router in the main application using `app.include_router()`.
- Uses `TestClient` to make a GET request to the endpoint and asserts its status code and JSON response.