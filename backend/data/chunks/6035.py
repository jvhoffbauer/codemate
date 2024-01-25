    def route_submit(self):
        async def route(request: Request, data: self.schema):  # type:ignore
            return await self.handle(request, data)  # type:ignore

        return route