@app.websocket("/items/{item_id}")
async def websocket_item(item_id: str, websocket: WebSocket):
    route: APIWebSocketRoute = websocket.scope["route"]
    await websocket.accept()
    await websocket.send_json({"item_id": item_id, "path": route.path})