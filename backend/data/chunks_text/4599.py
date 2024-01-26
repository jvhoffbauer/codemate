- This function takes three optional arguments (username, password, and scope).
- It makes a POST request to the "/token" endpoint with the provided credentials and scope (if specified).
- The response is parsed as JSON and the access token is extracted from it.
- The access token is returned by the function for further use in API requests.