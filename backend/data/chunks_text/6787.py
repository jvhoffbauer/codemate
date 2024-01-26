- Retrieves a user from the database using their email address with SQLAlchemy's `Session` and `select()`.
- Filters the results to match the provided email using an equality condition in the WHERE clause.
- Returns the first matching result as a `User` object or `None` if no matches are found.