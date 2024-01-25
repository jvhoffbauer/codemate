    def route_delete(self) -> Callable:
        async def route(
            request: Request,
            item_id: self.AnnotatedItemIdList,  # type: ignore
        ):
            if not await self.has_delete_permission(request, item_id):
                return self.error_no_router_permission(request)
            items = await self.delete_items(request, item_id)
            return BaseApiOut(data=len(items))

        return route