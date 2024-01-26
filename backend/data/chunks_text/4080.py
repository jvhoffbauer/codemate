- Tests a WebSocket connection with a session cookie using `TestClient`.
- Raises an exception (`WebSocketDisconnect`) when closing the WebSocket without sending any messages.
- Sends and receives multiple messages through the WebSocket to verify their content and associated metadata.