- This function is a GET request for all Hero objects from the database, using FastAPI's decorator `@app.get`.
- The returned data type is specified by `response_model`, which in this case is a list of `Hero` objects.
- The SQLAlchemy session manager (`Session`) is used to execute a SELECT query on the `Hero` table and retrieve all rows.