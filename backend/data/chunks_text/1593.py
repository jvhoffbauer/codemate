- This function is a GET request for retrieving all users from the database using FastAPI's decorator `@app.get`.
- It returns a list of user objects with schema defined in `schemas.User`, which can be customized by passing different arguments to the `response_model` parameter.
- The query parameters `skip` and `limit` are used to paginate through the results, allowing for efficient handling of large datasets without overloading the server or client.