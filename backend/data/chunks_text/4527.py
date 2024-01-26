- Retrieves an access token with scope'me' using `get_access_token`.
- Makes a GET request to '/users/me' with authorization header set to Bearer followed by the retrieved access token.
- Asserts that the status code is 200 and saves the response text for debugging purposes.
- Parses the JSON response body and asserts that it contains expected user attributes (username, full name, email, disabled).