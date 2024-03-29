- Generates an OpenAPI schema for a FastAPI application using `docstring` and `Pydantic` models as input.
- Exports the generated schema in JSON format at the endpoint `/openapi.json`.
- Defines a custom validation error model (`HTTPValidationError`) that inherits from the standard `ValidationError`, which is used to wrap HTTP errors with detailed information about their location and message.
- Includes a header parameter named `strange_header` that can be either a string or null, and provides two possible schemas for it based on different versions of `Pydantic`.