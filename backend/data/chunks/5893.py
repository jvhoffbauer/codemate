    def route_list(self) -> Callable:
        async def route(
            request: Request,
            sel: self.AnnotatedSelect,  # type: ignore
            paginator: Annotated[self.paginator, Depends()],  # type: ignore
            filters: Annotated[self.schema_filter, Body()] = None,  # type: ignore
        ):
            if not await self.has_list_permission(request, paginator, filters):
                return self.error_no_router_permission(request)
            data = ItemListSchema(items=[])
            data.query = request.query_params
            if await self.has_filter_permission(request, filters):
                data.filters = await self.on_filter_pre(request, filters)
                if data.filters:
                    sel = sel.filter(*self.calc_filter_clause(data.filters))
            if paginator.show_total:
                data.total = await self.db.async_scalar(
                    select(func.count("*")).select_from(
                        sel.with_only_columns(self.pk).subquery()
                    )
                )
            orderBy = self._calc_ordering(paginator.orderBy, paginator.orderDir)
            if orderBy:
                sel = sel.order_by(*orderBy)
            sel = sel.limit(paginator.perPage).offset(
                (paginator.page - 1) * paginator.perPage
            )
            result = await self.db.async_execute(sel)
            return BaseApiOut(data=await self.on_list_after(request, result, data))

        return route