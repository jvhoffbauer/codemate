    async def handle(
        self, request: Request, data: BaseModel, **kwargs
    ) -> BaseApiOut[Any]:
        ret = data.dict()
        return BaseApiOut(data={**ret, "extra": "success"})