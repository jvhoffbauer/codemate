    async def delete_items(
        self, request: Request, item_id: List[str]
    ) -> List[TableModelT]:
        """Delete the database data by id."""
        return await self.db.async_run_sync(self._delete_items, item_id)