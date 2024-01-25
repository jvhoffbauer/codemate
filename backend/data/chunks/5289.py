async def on_drawing(sid, data):
    await sio.emit("drawing", data, broadcast=True)