    async def create_items(
        self, request: Request, items: List[SchemaCreateT]
    ) -> List[TableModelT]:
        """Create multiple data"""
        exclude = await self.get_deny_fields(request, "create")
        items = [item.copy(exclude=exclude) for item in items]  # 过滤没有权限的字段
        items = await super().create_items(request, items)
        return items