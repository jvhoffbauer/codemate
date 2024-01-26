- Defines a FastAPI application and registers two identical endpoints with different URL paths (`/test1` and `/test2`) using decorators.
- Uses the built-in `TestClient` class to simulate HTTP requests against the application's server.
- Tests both endpoints separately by passing query parameters through the `params` dictionary in subsequent calls to `client.get`.
- Verifies that each endpoint returns the expected JSON response based on its corresponding query parameter value.