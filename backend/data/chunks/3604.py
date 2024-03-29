@prefix_router.websocket("/", dependencies=[create_dependency("routerprefixindex")])
async def routerprefixindex(websocket: WebSocket, deps: DepList):
    await websocket.accept()
    await websocket.send_text(json.dumps(deps))
    await websocket.close()