    async def get_list_columns(self, request: Request) -> List[TableColumn]:
        columns = await super().get_list_columns(request)
        for column in columns:
            if column and column.name in self.toggled_columns:
                column.toggled = False
        return columns