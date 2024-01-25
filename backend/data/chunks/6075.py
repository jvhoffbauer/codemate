    async def has_page_permission(
        self, request: Request, obj: "PageSchemaAdmin" = None, action: str = None
    ) -> bool:
        return await self.admin.has_action_permission(request, name=self.name)