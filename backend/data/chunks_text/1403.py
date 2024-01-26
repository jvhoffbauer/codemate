- Defines a custom exception handler for `RequestValidationError`.
- Returns a JSON response with HTTP status code 422 and error details when this exception is raised during request validation.
- Uses FastAPI's built-in `JSONResponse()` function to format the response as JSON.