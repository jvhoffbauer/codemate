    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)