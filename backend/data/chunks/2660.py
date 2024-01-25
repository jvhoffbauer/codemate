    async def catcher(websocket, call_next):
        try:
            return await call_next()
        except Exception as e:  # pragma: no cover
            caught.append(e)
            raise