- Generates an OpenAPI schema for a FastAPI application using `pytest` and `TestClient`.
- Verifies that the status code of the generated JSON is 200 and its content matches the expected structure.
- Extracts the necessary information from the API's endpoints to generate the schema, including responses, summaries, operation IDs, security requirements, etc.