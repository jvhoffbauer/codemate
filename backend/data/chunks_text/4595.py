- Tests if an incorrect token is provided in authorization header for getting user details (GET /users/me)
- Asserts that server returns HTTP status code 401 and error message 'Invalid authentication credentials'
- Verifies that WWW-Authenticate header contains Bearer value indicating use of bearer tokens