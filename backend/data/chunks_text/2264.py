- Attempts to connect to a websocket with an invalid path "/itemsx/portal-gun" using `client.websocket_connect()`.
- Raises a `WebSocketDisconnect` exception due to the incorrect path format, as per the WebSocket protocol specification.