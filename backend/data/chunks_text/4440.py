- Tests getting a list of users with an invalid token in the X-Token header
- Asserts that the status code is 400 Bad Request and the error message is "X-Token header invalid"
- Verifies that the JSON response contains the expected detail key and value