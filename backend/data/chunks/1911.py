    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)