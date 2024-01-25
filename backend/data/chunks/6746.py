    async def stream(self):
        async for body in self.request.stream():
            yield body