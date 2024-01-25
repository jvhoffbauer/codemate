    async def has_create_permission(
        self, request: Request, data: SchemaCreateT, **kwargs
    ) -> bool:  # type self.schema_create
        return await self.has_page_permission(request, action=CrudEnum.create)