- Retrieves a user with the given ID from the database using SQLAlchemy's `Session`.
- Checks whether the retrieved user is equal to the currently logged in user (stored in `current_user`) and returns it without further checks if they match. This prevents leaking sensitive information about other users.
- Raises an exception with a custom error message if the user trying to access this method isn't authorized to view arbitrary user records or has insufficient permissions. The exact status code for this error should be reviewed later.