    async def websocket(websocket: "WebSocket"):
        # Check we get the right headers back
        assert websocket.headers.get("x-request-id") is not None

        await websocket.accept()
        await websocket.send_json({"msg": "Hello WebSocket"})
        await websocket.close()