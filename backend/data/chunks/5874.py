    async def read_items(
        self, request: Request, item_id: List[str]
    ) -> List[SchemaReadT]:
        """Fetch the database data by id."""
        return await self.db.async_run_sync(self._read_items, item_id)