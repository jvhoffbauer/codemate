    async def get_list_filter(
        self, request: Request
    ) -> List[Union[SqlaField, FormItem]]:
        return self.list_filter or list(model_fields(self.schema_filter).values())