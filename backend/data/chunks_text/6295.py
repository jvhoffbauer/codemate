- Sets up and tears down a session object for HTTP requests using `httputils.setup_client_session()` and `httputils.teardown_client_session()`, respectively
- Verifies that `httputils.CLIENT_SESSION` is initially undefined, then defined after calling `httputils.setup_client_session()`
- Confirms that `httputils.CLIENT_SESSION` is closed after calling `httputils.teardown_client_session()`
- Deletes `httputils.CLIENT_SESSION` at the end of the test case