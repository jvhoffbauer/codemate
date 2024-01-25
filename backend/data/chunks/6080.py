    async def handle(
        self,
        request: Request,
        item_id: List[str],
        data: Optional[SchemaUpdateT],
        **kwargs,
    ) -> BaseApiOut[Any]:
        return BaseApiOut(data=data)