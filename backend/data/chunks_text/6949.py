- Creates a new user using FastAPI's `@router.post()` decorator and returns the created user as JSON using `response_model`.
- Requires authentication for superusers using `Depends(on_superuser)`.
- Checks if the provided email address already exists in the database using `crud_user.get()`, raising an error (HTTPException) if it does.
- Converts the plaintext password to a hash using `get_password_hash()` before storing it in the database.