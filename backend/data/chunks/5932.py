    async def has_filter_permission(
        self,
        request: Request,
        filters: Optional[SchemaFilterT],
        **kwargs,
    ) -> bool:
        return True