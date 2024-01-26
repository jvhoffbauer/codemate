- Retrieves user information for the currently authenticated user using FastAPI's dependency injection and `Depends()`.
- Returns the retrieved user object with a specified schema (in this case, `User`) as defined by the `response_model` parameter of the decorator.
- Uses the `GET /users/me/` endpoint to access the requested data.