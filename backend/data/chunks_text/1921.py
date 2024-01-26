- Defines a PUT endpoint for updating an item identified by its ID (stored in the path parameter `item_id`) using JSON request body (specified as `Body()` decorator).
- Uses FastAPI's built-in support for OpenAPI schema validation and documentation through the `Annotated[]` type hinting syntax.
- Provides examples of how to use this API endpoint via the `openapi_examples` dictionary passed into the `Body()` decorator. These examples are documented within the OpenAPI specification generated by FastAPI.