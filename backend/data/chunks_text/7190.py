- Creates a FastAPI application using `create_app()`.
- Wraps it in a test client (provided by PyTest's `TestClient`) and yields it for use in tests within this module scope.