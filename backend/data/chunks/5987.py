        async def route(
            request: Request,
            link_id: IdStrQuery,
            item_id: self.pk_admin.AnnotatedItemIdList,  # type: ignore
        ):
            if not await self.pk_admin.has_update_permission(request, item_id, None):
                return self.pk_admin.error_no_router_permission(request)
            values = []
            for item in map(get_python_type_parse(self.item_col), item_id):
                values.extend(
                    {self.link_col.key: link, self.item_col.key: item}
                    for link in map(
                        get_python_type_parse(self.link_col),
                        parser_str_set_list(link_id),
                    )
                )
            stmt = insert(self.link_model).values(values)
            try:
                result = await self.pk_admin.db.async_execute(stmt)
            except Exception as error:
                await self.pk_admin.db.async_rollback()
                return self.pk_admin.error_execute_sql(request=request, error=error)
            return BaseApiOut(data=result.rowcount)  # type: ignore