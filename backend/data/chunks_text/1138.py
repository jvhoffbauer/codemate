- This function handles a POST request to the `/token` endpoint and returns an Access Token in response. - The `OAuth2PasswordRequestForm` dependency is used to extract the username and password from the request body. - If the provided credentials are invalid, a 401 Unauthorized error with WWW-Authenticate header set to Bearer is returned. - Otherwise, an Access Token with an expiration time of ACCESS_TOKEN_EXPIRE_MINUTES minutes is created using the `create_access_token` function and returned along with the token type (Bearer).