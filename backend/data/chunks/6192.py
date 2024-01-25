    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        if not self.values:
            return sel
        column = getattr(admin.model, self.column)
        if len(self.values) == 1:
            return sel.where(column == self.values[0])
        return sel.where(column.in_(self.values))