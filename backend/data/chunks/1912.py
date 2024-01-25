    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)