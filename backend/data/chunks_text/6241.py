- Defines a pytest fixture named `api_client`.
- Returns an instance of FastAPI's built-in testing client, `TestClient`, which is used to make HTTP requests during tests.
- Uses the `requests` library internally to make these requests.