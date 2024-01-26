- Generates a JSON Web Token (JWT) for user authentication and authorization using Flask-JWT-Extended library's `create_access_token()` function.
- Sets an expiration time of access token based on `ACCESS_TOKEN_EXPIRE_MINUTES` setting in environment variables.
- Encodes JWT payload with user ID as a string value and secret key from AWS Secrets Manager. Uses HMAC SHA256 encryption algorithm specified by ALGORITHM variable.