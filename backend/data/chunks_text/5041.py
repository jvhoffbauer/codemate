- Listens for a "drawing" event from a client using Flask SocketIO's `@sio.on()` decorator
- Retrieves the drawing data (represented as JSON) sent by the client and saves it in the `data` variable
- Broadcasts the received drawing data to all connected clients via `await sio.emit()`, allowing them to see the real-time updates made by other users