- Tests if an HTTP GET request to `/items` with a query parameter `token=jessica` and an invalid X-Token header returns a 400 Bad Request status code and a JSON error message containing "X-Token header invalid".