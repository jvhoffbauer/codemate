- Defines a route with two possible URLs (/test1 and /test2) using FastAPI's decorator syntax (@app.get).
- Accepts a query parameter named 'var' of type str through the use of Pydantic's Annotated class.
- Returns a dictionary containing a key 'foo' whose value is the variable passed in as a query parameter ('bar' by default).