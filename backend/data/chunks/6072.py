    async def has_action_permission(self, request: Request, name: str) -> bool:
        if not await self.has_page_permission(request, action=name):
            return False
        elif name in {"delete", "bulk_delete"}:
            return await self.has_delete_permission(request, None)  # type: ignore
        elif name in {"update", "bulk_update"}:
            return await self.has_update_permission(request, None, None)  # type: ignore
        elif name in {"create", "bulk_create"}:
            return await self.has_create_permission(request, None)  # type: ignore
        elif name in {"read"}:
            return await self.has_read_permission(request, None)  # type: ignore
        else:
            return True