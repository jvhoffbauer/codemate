- Defines a function `client` that returns a generator
- Uses the context manager `with TestClient(app) as client:` to create and automatically close an instance of Flask's test client for the given app
- Yields the created client object, allowing it to be used in other parts of the program using the `send` method of generators