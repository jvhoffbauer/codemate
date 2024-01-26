- Tests that multiple query string parameters with the same name can be passed to a function using `List[str]`.
- Uses the `LowerCaseQueryStringMiddleware` middleware to convert all query string parameter keys and values to lowercase before passing them to functions.
- Demonstrates how to use the `TestClient` class from FastAPI's testing module to make requests against the application under test.