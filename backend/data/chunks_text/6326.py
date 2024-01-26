- Updates the password of the currently logged in user using their `UserUpdatePasswordRequest`.
- Hashes the new password and sets it as the updated value for the `hashed_password` attribute on the current user object.
- Adds the modified user to the database session and commits the changes.
- Returns the updated user object.