    async def create_items(
        self, request: Request, items: List[SchemaCreateT]
    ) -> List[TableModelT]:
        """Create multiple database data."""
        items = [await self.on_create_pre(request, obj) for obj in items]
        return await self.db.async_run_sync(self._create_items, items)