- Creates a new user with a randomly generated email and password using `UserCreate`.
- Saves the newly created user to the database using `crud.user.create`.
- Asserts that the saved user's email matches the input email.
- Checks if the saved user object contains an attribute named 'hashed_password'.