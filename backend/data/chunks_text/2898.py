- Generates an OpenAPI schema for a FastAPI application using `fastapi.encoders.jsonable_encoder`.
- The generated JSON schema conforms to the OpenAPI Specification version 3.1.0 (OAS3).
- Includes information about the API's title and version in the `info` object.
- Defines endpoints with their corresponding HTTP methods, request parameters, responses, and error handling mechanisms.
- Uses Pydantic data models as input schemas for requests and responses.
- Provides detailed documentation of each endpoint through summary, operation ID, and description fields.
- Implements validation errors according to OAS3 standards by defining custom error types and providing examples of how they should be structured.