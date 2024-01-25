        async def route(request: Request, data: self.schema):  # type:ignore
            return await self.handle(request, data)  # type:ignore