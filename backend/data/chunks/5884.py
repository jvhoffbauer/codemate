    async def on_list_after(
        self, request: Request, result: Result, data: ItemListSchema, **kwargs
    ) -> ItemListSchema:
        """Parse the database data query result dictionary into schema_list."""
        data.items = self.parser.conv_row_to_dict(result.all())
        data.items = [self.list_item(item) for item in data.items]
        return data