@app.websocket("/", dependencies=[create_dependency("index")])
async def index(websocket: WebSocket, deps: DepList):
    await websocket.accept()
    await websocket.send_text(json.dumps(deps))
    await websocket.close()