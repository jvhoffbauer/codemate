- Defines an asynchronous function called `http_exception_handler`.
- Takes in a request object and an instance of the built-in FastAPI exception class `HTTPException`.
- Returns a JSON response with a customized message based on the details provided by the `HTTPException`. The status code is also set to match that of the exception.