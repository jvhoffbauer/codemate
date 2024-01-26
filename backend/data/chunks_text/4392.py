- Generates an OpenAPI schema for a FastAPI application using Pytest and TestClient to make requests and verify responses.
- The generated schema includes information about endpoints (e.g., `GET /items/`) with their corresponding HTTP methods, request parameters, and expected responses (including error codes).
- The schema also defines custom validation errors that can be returned by the API, as well as any required headers or cookies.