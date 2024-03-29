- Uses `pydanticv2` to validate and parse JSON data in a FastAPI endpoint's response for model'modelA'.
- Retrieves the response from the API using `TestClient`.
- Asserts that the status code is 200 and checks if the expected JSON response matches with the actual one received. Additionally, it extracts the nested sub-model 'foo' containing the username value 'test-user'.