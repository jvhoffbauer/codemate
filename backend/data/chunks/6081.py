    @property
    def route_submit(self):
        async def route(
            request: Request,
            item_id: self.admin.AnnotatedItemIdList,  # type:ignore
            data: Annotated[self.schema, Body()] = None,  # type:ignore
        ):
            return await self.handle(request, item_id, data)

        return route