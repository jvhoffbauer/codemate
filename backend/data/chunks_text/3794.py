- Defines an OpenAPI schema for a FastAPI application with version 3.1.0
- Includes information about the API's title and version
- Describes the GET request to the `/portal` endpoint, including its summary, operation ID, parameters (including one optional boolean parameter), responses (with success and validation error cases), and content types
- Defines two schemas for HTTP errors: `HTTPValidationError`, which is an array of `ValidationErrors`, and `ValidationError`, which includes location, message, and type fields