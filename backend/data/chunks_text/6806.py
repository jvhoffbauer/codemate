- Retrieves an `Item` object with the given `ID` from the database using a SQLAlchemy `Session`.
- Raises a `HTTPException` with status code 404 if the item is not found in the database.
- Checks whether the user has sufficient permissions to access the item based on its owner ID and their own ID. If they are not the superuser and the item's owner is different than themselves, raises another `HTTPException` with status code 400 and a custom error message. Otherwise, returns the retrieved `Item` as output.