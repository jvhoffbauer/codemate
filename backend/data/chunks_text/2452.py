- Tests synchronous endpoint that raises a server error (500 status code). - Uses `TestClient` with `raise_server_exceptions=False`. - Asserts that expected HTTP status code and text are returned by the API. - Verifies that the generator's finalization is executed as expected. - Clears the errors dictionary to ensure it doesn't interfere with other tests.