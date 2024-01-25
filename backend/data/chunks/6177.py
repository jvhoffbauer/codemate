    async def on_update_pre(
        self,
        request: Request,
        obj: SchemaUpdateT,
        item_id: Union[List[str], List[int]],
        **kwargs,
    ) -> Dict[str, Any]:
        exclude = await self.get_deny_fields(request, "update")  # 过滤没有权限的字段
        obj = obj.copy(exclude=exclude)  # 过滤没有权限的字段
        data = await super().on_update_pre(request, obj, item_id, **kwargs)
        return data