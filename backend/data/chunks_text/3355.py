- Defines a new endpoint `/` with an HTTP POST method using FastAPI's decorator syntax
- Accepts a JSON request body of type `test_type`, which is defined elsewhere in the application
- Returns the received data as-is, converted to the expected output format (in this case, also `test_type`)