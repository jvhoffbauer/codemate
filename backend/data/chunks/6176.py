    async def read_items(
        self, request: Request, item_id: List[str]
    ) -> List[SchemaReadT]:
        """Read multiple data"""
        items = await super().read_items(request, item_id)
        exclude = await self.get_deny_fields(request, "read")  # 过滤没有权限的字段
        return [item.copy(exclude=exclude) for item in items]