    async def has_action_permission(self, request: Request, name: str) -> bool:
        return await self.has_page_permission(request, action=name)