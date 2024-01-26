- Uses `pytest-mock` to simulate HTTP requests and responses for testing purposes
- Retrieves a list of users from the API using GET request at "/users/" endpoint
- Verifies that the status code is 200 (OK) and checks if required fields ("email" and "id") are present in the first user's JSON representation returned by the server