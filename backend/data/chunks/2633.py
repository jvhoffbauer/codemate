@native_prefix_route.websocket("/")
async def router_native_prefix_ws(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello, router with native prefix!")
    await websocket.close()