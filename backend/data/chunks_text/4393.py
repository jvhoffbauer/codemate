- Generates an OpenAPI (Swagger) JSON schema for a FastAPI application using `docstring` and `Pydantic` models as input.
- Defines endpoints with request parameters, responses, status codes, and summary descriptions.
- Includes support for cookie-based query parameters through `CookieParam`.
- Provides error handling by defining custom validation errors and mapping them to HTTP status codes.
- Exposes the generated schema under the `/openapi.json` endpoint.