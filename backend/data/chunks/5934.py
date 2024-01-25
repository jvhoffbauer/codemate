    async def has_read_permission(
        self, request: Request, item_id: Optional[List[str]], **kwargs
    ) -> bool:
        return True