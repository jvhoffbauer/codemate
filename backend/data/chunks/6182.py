    async def filter_select(self, request: Request, sel: Select) -> Select:
        """在sel中添加权限过滤条件"""
        for permission in self.select_permissions:
            if not isinstance(permission, SelectPerm):
                continue
            effect = await self.has_select_permission(request, permission.name)
            # 如果权限为反向权限,则判断用户是否没有权限
            if permission.reverse ^ effect:
                sel = permission.call(self, request, sel)
                if asyncio.iscoroutine(sel):
                    sel = await sel
        return sel