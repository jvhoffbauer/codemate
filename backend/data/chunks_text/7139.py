- This function implements simple login functionality and can be extended with complex business logic by moving it to a separate `logic` folder.
- It takes a request object containing the username (phone number in this case) and password as input.
- The function first verifies the user's credentials using a hypothetical `User` model and `security` module for password verification. If the user is not found or the password is incorrect, an error response is returned.
- Otherwise, an access token is generated using the `security` module and stored along with the user ID. The token has an expiration time of `settings.ACCESS_TOKEN_EXPIRE_MINUTES`.
- In place of the hardcoded implementation, a more complex business logic can be implemented in a separate file called `UserLogic`, which returns the token after successful authentication.