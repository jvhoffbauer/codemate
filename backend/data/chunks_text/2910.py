- Tests if `GET /openapi.json` returns a successful HTTP response with status code 200 OK
- Compares the JSON response to a predefined schema and asserts equality
- Asserts that there is exactly one parameter in the GET request for the endpoint `/`, which matches our expected design