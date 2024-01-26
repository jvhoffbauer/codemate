- Creates an `AsyncGenerator` fixture named `async_client` that yields a new instance of `AsyncClient` for each test case using the FastAPI application provided by the `AdminSite`.
- Sets the base URL to "http://testserver" for the `AsyncClient`, which is used when making requests during tests.
- The generated `AsyncClient` object can be accessed in individual test functions through the `async_client` fixture.