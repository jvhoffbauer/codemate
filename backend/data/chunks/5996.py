    async def has_page_permission(
        self, request: Request, obj: "PageSchemaAdmin" = None, action: str = None
    ) -> bool:
        return self.app is self or await self.app.has_page_permission(
            request, obj=obj or self, action=action
        )