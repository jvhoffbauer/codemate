- Tests retrieving an existing user using a GET request with authentication as a superuser
- Creates a new user in the database and gets its ID
- Makes a GET request to retrieve the user by ID with the superuser token headers
- Asserts that the response status is within the expected range (2xx)
- Extracts the JSON data from the response body
- Retrieves the same user from the database by email
- Asserts that both the API user and the database user have the same email address