    async def update_items(
        self, request: Request, item_id: List[str], values: Dict[str, Any]
    ) -> List[TableModelT]:
        """Update the database data by id."""
        return await self.db.async_run_sync(self._update_items, item_id, values)