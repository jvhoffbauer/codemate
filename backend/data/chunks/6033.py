        async def route(request: Request):
            return await self.get_init_data(request)