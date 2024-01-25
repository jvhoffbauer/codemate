    async def handle(
        self, request: Request, data: SchemaUpdateT, **kwargs
    ) -> BaseApiOut[Any]:
        return BaseApiOut(data=data)