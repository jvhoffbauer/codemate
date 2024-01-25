    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        if not self.filters:
            return sel
        return sel.filter(*self.filters)