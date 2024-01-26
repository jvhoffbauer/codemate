- Defines a function `get_auth_user()` with an optional argument `auth_token`.
- If `auth_token` is missing or empty, raises an exception `AuthError`.
- Otherwise, retrieves the user associated with the given token using another helper function `get_user_by_token()`, and returns it. Raises `KeyError` if the token is invalid.