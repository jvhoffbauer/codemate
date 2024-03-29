- Creates a new user with a randomly generated username and password using `UserCreate`.
- Saves the user to the default GAE datastore using `crud.user.upsert`.
- Asserts that the saved user object contains attributes for its username, hashed password, and type (which is set to 'userprofile' by default).