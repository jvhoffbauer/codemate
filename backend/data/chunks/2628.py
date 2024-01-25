@router.websocket("/router/{pathparam:path}")
async def routerindexparams(websocket: WebSocket, pathparam: str, queryparam: str):
    await websocket.accept()
    await websocket.send_text(pathparam)
    await websocket.send_text(queryparam)
    await websocket.close()