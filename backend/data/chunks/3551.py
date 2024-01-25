    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or self.max_content_size is None:
            await self.app(scope, receive, send)
            return

        wrapper = self.receive_wrapper(receive)
        await self.app(scope, wrapper, send)