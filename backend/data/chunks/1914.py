    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)