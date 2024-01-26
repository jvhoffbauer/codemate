- Tests if a request with an invalid body embedded in another object results in a 422 status code (Unprocessable Entity)
- Uses Flask's built-in `client` to simulate a POST request to the "/body-embed" endpoint with an invalid JSON payload containing an "invalid" key
- Asserts that the server returns a HTTP 422 error status code for the given input