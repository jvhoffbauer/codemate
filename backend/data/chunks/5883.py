    async def on_filter_pre(
        self, request: Request, obj: Optional[SchemaFilterT], **kwargs
    ) -> Dict[str, Any]:
        return obj and {
            k: v
            for k, v in obj.dict(exclude_unset=True, by_alias=True).items()
            if v is not None
        }