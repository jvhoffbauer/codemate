- Defines a GET endpoint with specific path and response model (User).
- Uses FastAPI's `response_model` decorator to automatically validate input/output data based on User schema.
- Returns an instance of DBUser class that conforms to User schema, which can be used for further processing or storage in a database.