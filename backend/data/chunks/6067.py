    async def has_filter_permission(
        self,
        request: Request,
        filters: Optional[SchemaFilterT],
        **kwargs,
    ) -> bool:
        return await self.has_page_permission(request, action=CrudEnum.filter)