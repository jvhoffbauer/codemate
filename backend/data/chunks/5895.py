    @property
    def route_create(self) -> Callable:
        async def route(
            request: Request,
            data: Annotated[Union[List[self.schema_create], self.schema_create], Body()],  # type: ignore
        ) -> BaseApiOut[Union[int, self.schema_model]]:  # type: ignore
            if not await self.has_create_permission(request, data):
                return self.error_no_router_permission(request)
            if not isinstance(data, list):
                data = [data]
            try:
                items = await self.create_items(request, data)
            except Exception as error:
                await self.db.async_rollback()
                return self.error_execute_sql(request=request, error=error)
            result = len(items)
            if result == 1:  # if only one item, return the first item
                result = await self.db.async_run_sync(
                    lambda _: parse_obj_to_schema(
                        items[0], self.schema_model, refresh=True
                    )
                )
            return BaseApiOut(data=result)

        return route