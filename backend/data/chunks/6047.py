    async def get_list_columns(self, request: Request) -> List[TableColumn]:
        columns = []
        for field in await self.get_list_display(request):
            column = None
            if isinstance(field, BaseAmisModel):
                column = field
            else:
                modelfield = self.parser.get_modelfield(field)
                if modelfield:
                    column = await self.get_list_column(request, modelfield)
            if column:
                columns.append(column)
        return columns