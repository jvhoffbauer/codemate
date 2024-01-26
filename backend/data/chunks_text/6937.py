- This function retrieves the current authenticated user from a JWT token and an SQLAlchemy database session using FastAPI's dependency injection system. - It first extracts the user ID from the token using `get_token_data`, which is a built-in middleware provided by FastAPI for handling JWT tokens. - The function then calls `crud_user.get()` to retrieve the corresponding user object from the database based on the extracted user ID. - If the user is not found or has been deactivated, it raises a customized HTTP exception with appropriate error messages. - Otherwise, the active user object is returned as the result of this function.