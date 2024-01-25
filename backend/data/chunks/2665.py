    async def custom_handler(websocket: WebSocket, exc: CustomError) -> None:
        await websocket.close(1002, "foo")