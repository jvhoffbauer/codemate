- Creates a new user with a randomly generated email and password using `UserCreate`.
- Saves the newly created user to the database using `crud.user.create`.
- Checks if the newly created user has superuser privileges using `crud.user.is_superuser`.
- Asserts that the returned boolean value from `crud.user.is_superuser` should be false for normal users.