    async def has_list_permission(
        self,
        request: Request,
        paginator: Optional[Paginator],
        filters: Optional[SchemaFilterT],
        **kwargs,
    ) -> bool:
        return True