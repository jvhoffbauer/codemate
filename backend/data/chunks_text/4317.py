- Tests if the OpenAPI schema can be retrieved successfully by making a GET request to `/openapi.json`.
- Asserts that the status code is 200 and checks the text of the response in case of failure.
- Verifies that the JSON returned from the API matches the expected format for an OpenAPI v3.1.0 specification with specific details about the root endpoint (`GET /`) provided.