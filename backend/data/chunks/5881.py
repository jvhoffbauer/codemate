    async def on_create_pre(
        self, request: Request, obj: SchemaCreateT, **kwargs
    ) -> Dict[str, Any]:
        data = obj.dict(by_alias=True)  # exclude=set(self.pk)
        if self.pk_name in data and not data.get(self.pk_name):
            del data[self.pk_name]
        return data