    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        glb.reset()
        await self.app(scope, receive, send)