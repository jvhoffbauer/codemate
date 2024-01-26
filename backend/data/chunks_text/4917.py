- Creates a new user with a randomly generated email and password using `UserCreate`.
- Saves the user to the default GAE datastore using `crud.user.upsert`.
- Retrieves the newly created user from the datastore using `crud.user.get`.
- Checks if the retrieved user's active flag is true using `crud.user.is_active`.
- Asserts that the active flag is indeed true.