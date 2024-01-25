@dataclass
class UserSelectPerm(SelectPerm):
    """所属用户选择数据集,只能选择匹配当前用户的数据"""

    user_column: str = "user_id"
    user_attr: str = "id"

    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        user = await admin.site.auth.get_current_user(request)
        if not user:  # 未登录
            return sel.where(False)
        column = getattr(admin.model, self.user_column)
        return sel.where(column == getattr(user, self.user_attr))