- Defines an asynchronous function `update_user` that takes three arguments: `user_id`, `user_in`, and a dependency for getting the database session (`session`) from FastAPI's `Depends()`.
- Retrieves the existing user object from the database using `crud_user.get()`. If it doesn't exist, raises a customized HTTP exception with error message.
- Updates the user object using `crud_user.update()` with the new data provided by `user_in` and hashes the password again to ensure security.
- Handles any potential integrity errors during the update process by raising another customized HTTP exception.