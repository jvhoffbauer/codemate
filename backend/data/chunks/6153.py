    async def has_delete_permission(
        self, request: Request, item_id: List[str], **kwargs
    ) -> bool:
        return False