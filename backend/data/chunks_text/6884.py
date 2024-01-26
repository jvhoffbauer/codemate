- Initializes a Flask application using `get_app()`.
- Creates a new instance of Flask's built-in testing client, `TestClient`, and passes in the initialized app for integration tests.
- Yields the created `test_client` object to allow multiple context managers to use it simultaneously during testing.