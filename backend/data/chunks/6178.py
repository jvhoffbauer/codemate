    async def get_form_item(
        self, request: Request, modelfield: ModelField, action: CrudEnum
    ) -> Union[FormItem, SchemaNode, None]:
        """过滤前端创建,更新,筛选表单字段"""
        # action为list时,表示列表展示字段.否则为筛选表单字段
        act = "filter" if action == "list" else action
        exclude = await self.get_deny_fields(request, act)  # 获取没有权限的字段
        name = modelfield.alias or modelfield.name
        if name in exclude:
            return None
        form_item = await super().get_form_item(request, modelfield, action)
        return form_item