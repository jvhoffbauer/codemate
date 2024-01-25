    async def has_field_permission(
        self, request: Request, field: str, action: str = ""
    ) -> bool:
        """判断用户是否有字段权限"""
        return True