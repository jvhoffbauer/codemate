- Tests retrieving user information with an authorization token
- Uses Flask's built-in `TestClient` to simulate a request from a client
- Asserts that the status code is 200 and checks the JSON response matches expected values for the authenticated user 'johndoe'