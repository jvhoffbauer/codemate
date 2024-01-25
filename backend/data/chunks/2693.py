async def get_value_by_ws(
    websocket: WebSocket, value: int = Depends(extract_value_from_http_connection)
):
    await websocket.accept()
    await websocket.send_json(value)
    await websocket.close()