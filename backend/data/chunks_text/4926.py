- Creates a new user with a randomly generated username and password using superuser privileges
- Sends a POST request to the /users endpoint of the API with the user's details as JSON payload
- Asserts that the response status is within the range of successful HTTP responses (2xx)
- Retrieves the newly created user from the database using their username and checks if its properties match those returned by the API