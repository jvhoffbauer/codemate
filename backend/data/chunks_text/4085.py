- Tests connecting to a websocket without credentials using PyTest's `TestClient`.
- Raises `WebSocketDisconnect` exception during connection establishment due to missing authentication credentials.
- Prevents further execution of the function body by raising an assertion error (`pytest.fail`) if the expected exception is not raised, ensuring that tests are robust and reliable.