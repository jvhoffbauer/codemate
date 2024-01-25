    async def has_select_permission(self, request: Request, name: str) -> bool:
        """判断用户是否有数据集权限"""
        return True