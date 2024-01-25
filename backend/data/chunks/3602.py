@router.websocket("/router", dependencies=[create_dependency("routerindex")])
async def routerindex(websocket: WebSocket, deps: DepList):
    await websocket.accept()
    await websocket.send_text(json.dumps(deps))
    await websocket.close()