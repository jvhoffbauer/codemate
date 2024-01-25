    async def get_list_display(
        self, request: Request
    ) -> List[Union[SqlaField, TableColumn]]:
        return self.list_display or list(model_fields(self.schema_list).values())