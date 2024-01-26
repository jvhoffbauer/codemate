- Sends a POST request to "/cookie-and-object/" endpoint using Flask's built-in `client` object.
- Asserts that the status code of the response is 200 and saves its text for debugging purposes.
- Extracts the JSON response body and asserts it matches the expected value.
- Accesses the cookie named 'fakesession' from the response headers and asserts its value matches an expected string.