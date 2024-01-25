    async def get_link_clause(
        self,
        request: Request,
        link_model: str = None,
        link_item_id: IdStrQuery = None,
        op: Literal["in_", "not_in", None] = None,
    ) -> Optional[Any]:
        if link_model and link_item_id:
            result = self.link_models.get(link_model)
            if not result:
                return None
            table, pk_col, link_col = result
            if table is not None:
                link_item_id = list(
                    map(
                        get_python_type_parse(link_col),
                        parser_str_set_list(link_item_id),
                    )
                )
                if op == "not_in":
                    return self.pk.not_in(
                        select(pk_col).where(link_col.in_(link_item_id))
                    )
                else:
                    return self.pk.in_(select(pk_col).where(link_col.in_(link_item_id)))
        return None