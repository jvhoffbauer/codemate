    async def has_list_permission(
        self,
        request: Request,
        paginator: Paginator,
        filters: SchemaFilterT = None,
        **kwargs,
    ) -> bool:
        return await self.has_page_permission(request, action=CrudEnum.list)