- Retrieves a specific user with the given `username` from the database using FastAPI's built-in dependency injection and SQLAlchemy ORM.
- Checks whether the requested user is equal to the authenticated user retrieved through `Depends(get_current_active_user)`. If so, returns the user object directly.
- Verifies that the authenticated user has sufficient permissions to access this resource based on their role in the system. Raises an error otherwise.