- Tests closing websocket connection due to invalid data in URL parameters using `pytest.raises()`.
- Uses `TestClient` from Pytest's built-in testing framework for making requests and connecting to web sockets.
- Raises a `WebSocketDisconnect` exception if the connection is successfully established, indicating that the URL parameters are invalid.