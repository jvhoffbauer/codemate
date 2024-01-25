    async def page_permission_depend(self, request: Request) -> bool:
        return await self.has_page_permission(
            request, action="page"
        ) or self.error_no_page_permission(request)