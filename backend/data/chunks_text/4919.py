- Creates a new user with superuser role using `UserCreate` and `crud.user.upsert`.
- Retrieves the created user from the database using `get_default_bucket()`, `crud.user.upsert()`, and `persist_to=1`.
- Checks if the retrieved user has superuser privileges using `crud.user.is_superuser()`.
- Asserts that the returned value of `crud.user.is_superuser()` is true for the newly created superuser.