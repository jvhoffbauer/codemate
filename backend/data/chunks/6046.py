    async def get_list_column(
        self, request: Request, modelfield: ModelField
    ) -> TableColumn:
        column = self.amis_parser.as_table_column(modelfield)
        if await self.has_update_permission(request, None, None) and modelfield.name in model_fields(  # type: ignore
            self.schema_update
        ):
            if column.type == "switch":
                column.disabled = False
            column.quickEdit = await self.get_column_quick_edit(request, modelfield)
        return column