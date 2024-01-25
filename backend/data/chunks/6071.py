    async def has_delete_permission(
        self, request: Request, item_id: List[str], **kwargs
    ) -> bool:
        return await self.has_page_permission(request, action=CrudEnum.delete)