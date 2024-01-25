    @websocket_middleware
    async def errorhandler(websocket: WebSocket, call_next):
        try:
            return await call_next()
        except Exception as e:
            await websocket.close(code=status.WS_1006_ABNORMAL_CLOSURE, reason=repr(e))