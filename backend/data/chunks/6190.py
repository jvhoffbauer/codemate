    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        user = await admin.site.auth.get_current_user(request)
        if not user:  # 未登录
            return sel.where(False)
        column = getattr(admin.model, self.user_column)
        return sel.where(column == getattr(user, self.user_attr))