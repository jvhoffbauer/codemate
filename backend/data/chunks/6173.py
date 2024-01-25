    async def on_list_after(
        self, request: Request, result: Result, data: ItemListSchema, **kwargs
    ) -> ItemListSchema:
        """Parse the database data query result dictionary into schema_list."""
        exclude = await self.get_deny_fields(request, "list")  # 过滤没有权限的字段
        data = await super().on_list_after(request, result, data, **kwargs)
        data.items = [item.dict(exclude=exclude) for item in data.items]  # 过滤没有权限的字段
        return data