async def router_ws_depends_validate(
    websocket: WebSocket, data=Depends(ws_dependency_validate)
):
    pass  # pragma: no cover