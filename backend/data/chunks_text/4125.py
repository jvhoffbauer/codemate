- Generates an OpenAPI (Swagger) JSON schema for a FastAPI application using Pytest and Pydantic.
- The `test_openapi_schema` function tests that the generated schema is correct by making a GET request to the `/openapi.json` endpoint of the app and checking its status code and content against expected values.
- The schema includes definitions for the main components of the API, such as paths, responses, parameters, and error types.
- The schema follows the latest version of the OpenAPI specification (v3.1.0).