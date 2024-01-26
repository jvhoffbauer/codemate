- This fixture is automatically called by `pytest_asyncio` and sets up an `AsyncSession` object named `session`.
- The `yield` statement returns control to the caller of this function until it's time to clean up resources (in this case, at the end).
- After the tests are completed, all rows in every table defined by SQLAlchemy's metadata are deleted using a loop over the `Base.metadata.tables` dictionary.
- Finally, any changes made during testing are committed to the database.