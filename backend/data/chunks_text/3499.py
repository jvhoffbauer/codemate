- Tests if accessing a protected resource without credentials returns a specific error message and status code (401 Unauthorized)
- Uses Flask's built-in `client` object to simulate HTTP requests from outside the application
- Verifies that the expected JSON response is returned with the correct error message