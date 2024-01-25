    async def on_filter_pre(
        self, request: Request, obj: Optional[SchemaFilterT], **kwargs
    ) -> Dict[str, Any]:
        data = await super().on_filter_pre(request, obj, **kwargs)
        if not data:
            return data
        exclude = await self.get_deny_fields(request, "filter")  # 过滤没有权限的字段
        return {k: v for k, v in data.items() if k not in exclude}