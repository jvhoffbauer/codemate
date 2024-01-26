- Defines an asynchronous function called `http_exception_handler`.
- Takes two arguments - a request object and an exception object (`exc`) representing HTTP exceptions raised by FastAPI's built-in error handling mechanism.
- Returns a plain text response with the exception detail string and its corresponding HTTP status code using the `PlainTextResponse()` class from FastAPI's responses module.