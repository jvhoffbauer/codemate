- Tests login with incorrect password using `TestClient`.
- Sends a POST request to `/token` endpoint with invalid credentials (wrong password).
- Asserts that server returns HTTP status code 400 and error message "Incorrect username or password".