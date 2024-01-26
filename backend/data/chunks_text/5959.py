- Creates an `AsyncClient` object for a FastAPI app running on test server (localhost by default).
- Yields the client to be used in other functions or context managers that require it.
- Automatically closes and cleans up resources when done using the generator context manager syntax.