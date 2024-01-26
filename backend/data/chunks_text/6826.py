- Defines a function `test_token()` that takes a dependency `models.User` from `Depends(deps.get_current_user)`.
- The returned value of this function is any type, which can be used for further processing in other functions or endpoints.
- This function serves as a way to test and verify the user's authentication status using an access token obtained through OAuth2 authorization flow.