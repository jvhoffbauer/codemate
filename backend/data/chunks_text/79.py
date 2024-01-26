1. Defines an asynchronous function `exec()` that executes a SQL query or command using the synchronous session's `exec()` method wrapped in a Greenlet (async coroutine) to make it asynchronous.
2. Accepts three arguments - the SQL statement, optional parameters for the statement, and optional execution options.
3. Merges the provided execution options with default ones before passing them to the underlying `exec()`.
4. Spawns a new Greenlet to execute the SQL operation and returns its value after waiting for it to complete synchronously.
5. Wraps the returned Result object from the synchronous session's `exec()` in another helper function called `_ensure_sync_result()` to ensure it is synchronized properly.