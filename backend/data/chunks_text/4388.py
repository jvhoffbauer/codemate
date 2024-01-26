- Generates an OpenAPI schema for a FastAPI application using Pytest and TestClient to make requests and verify responses.
- The generated schema includes information about endpoints (e.g., `GET /items/`) with their corresponding HTTP methods, request parameters, and response codes and bodies.
- The schema also defines custom error types (such as `HTTPValidationError`) that are used by FastAPI's validation system. These errors can be referenced in other parts of the schema using JSON references ($ref).