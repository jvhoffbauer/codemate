- Tests if incorrect password can log in using POST request to `/admin/auth/login/access-token` endpoint with provided JSON data containing username and password
- Asserts that expected HTTP status code of 200 is returned, indicating successful API call
- Asserts that expected error code (4003) is included in response JSON