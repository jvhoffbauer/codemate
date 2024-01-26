- Tests that a POST request with JSON body creates an item and returns its ID in the Location header
- Asserts that the status code is 200 and checks the response text for debugging purposes (optional)
- Verifies that the returned JSON contains the expected data structure, including nested fields like `IsOneOf` validators from Pydantic's `v1_openapi` schema format (deprecated as of version 1.9)