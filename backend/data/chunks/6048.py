    async def _get_list_columns_for_link_model(self, request) -> List[ColumnOperation]:
        columns = []
        for link_form in self.link_model_forms:
            form = await link_form.get_form_item(request)
            if not form:
                continue
            columns.append(
                ColumnOperation(
                    width=160,
                    label=link_form.display_admin.page_schema.label,
                    breakpoint="*",
                    buttons=[form],
                )
            )
        return columns