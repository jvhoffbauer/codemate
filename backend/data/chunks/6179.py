    async def get_list_column(
        self, request: Request, modelfield: ModelField
    ) -> Optional[TableColumn]:
        """过滤前端展示字段"""
        exclude = await self.get_deny_fields(request, "list")  # 获取没有权限的字段
        name = modelfield.alias or modelfield.name
        if name in exclude:
            return None
        column = await super().get_list_column(request, modelfield)
        return column