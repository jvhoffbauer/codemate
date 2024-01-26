- Creates a new user with a randomly generated email and password using `UserCreate`.
- Saves the newly created user to the database using `crud.user.create`.
- Retrieves the active status of the saved user using `crud.user.is_active`.
- Asserts that the retrieved active status is true.