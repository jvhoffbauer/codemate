    async def has_update_permission(
        self,
        request: Request,
        item_id: Optional[List[str]],
        obj: Optional[SchemaUpdateT],
        **kwargs,
    ) -> bool:
        return True