- Sets up and tears down a global `ClientSession` object using decorators provided by PyTest's fixtures feature (`pytest.fixture`)
- Raises an AttributeError if `CLIENT_SESSION` is accessed before it has been defined, ensuring that tests cannot accidentally rely on its existence before initialization
- Asserts that `CLIENT_SESSION` exists after initialization but before teardown
- Asserts that `CLIENT_SESSION` is closed after teardown
- Deletes `CLIENT_SESSION` from memory to prevent resource leaks or unexpected behavior in future tests