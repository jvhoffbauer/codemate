1. Clears global variables and checks if testing environment is set up correctly by ensuring that there are no databases present.
2. Raises an error when trying to access synchronous or asynchronous databases without setting a site first.
3. Sets the current site and verifies that the database is not yet created.
4. Attempts to retrieve both synchronous and asynchronous databases but raises errors for each since they have not been initialized yet.
5. Retrieves the asynchronous database associated with the currently active site using `getattr`.
6. Verifies that the retrieved object is of type `AsyncDatabase`.
7. Initializes a new synchronous database and sets it globally.
8. Confirms that the newly added synchronous database exists while checking that the asynchronous one still doesn't exist.
9. Accesses the previously set synchronous database and confirms its identity.
10. Tries to reinitialize the same synchronous database again but fails due to already being set.