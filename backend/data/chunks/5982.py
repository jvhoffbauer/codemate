    @property
    def route_delete(self):
        async def route(
            request: Request,
            link_id: IdStrQuery,
            item_id: self.pk_admin.AnnotatedItemIdList,  # type: ignore
        ):
            if not await self.pk_admin.has_update_permission(request, item_id, None):
                return self.pk_admin.error_no_router_permission(request)
            stmt = (
                delete(self.link_model)
                .where(
                    self.link_col.in_(
                        list(
                            map(
                                get_python_type_parse(self.link_col),
                                parser_str_set_list(link_id),
                            )
                        )
                    )
                )
                .where(
                    self.item_col.in_(
                        list(map(get_python_type_parse(self.item_col), item_id))
                    )
                )
            )
            result = await self.pk_admin.db.async_execute(stmt)
            return BaseApiOut(data=result.rowcount)  # type: ignore

        return route