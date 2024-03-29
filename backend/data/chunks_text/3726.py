- Defines a module-scoped fixture named `client` using PyTest's built-in `temp_path_factory`.
- Creates a temporary directory for storing data and sets it as the current working directory (CWD).
- Initializes an instance of the SQL application, which creates a new database file in the CWD.
- Reloads the imported module to ensure that any necessary setup is executed during each test run.
- Yields the created Flask test client object for use within tests.
- Deletes the generated database file at the end of the test session.
- Restores the original CWD before returning control to the caller.