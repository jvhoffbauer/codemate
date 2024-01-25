    def route_init(self):
        async def route(request: Request):
            return await self.get_init_data(request)

        return route