- Tests if authentication with incorrect password fails and returns a 401 Unauthorized status code with an error message in JSON format.
- Uses the `raw_request` function to simulate sending a request with wrong credentials.
- Asserts that the response's status code is 401 and its content matches the expected error message.