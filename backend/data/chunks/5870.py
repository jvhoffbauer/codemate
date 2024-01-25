    async def fetch_items(self, *item_id: str) -> List[TableModelT]:
        """Fetch the database data by id."""
        return await self.db.async_run_sync(self._fetch_item_scalars, item_id)