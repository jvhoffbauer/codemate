- Creates a new user using `crud.user.create()`.
- Checks for existing users with the same email address using `crud.user.get_by_email()`. If found, raises an error.
- Sends a welcome email to the newly created user's email address (optional).