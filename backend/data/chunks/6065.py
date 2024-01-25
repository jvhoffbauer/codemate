    async def get_page(self, request: Request) -> Page:
        page = await super(ModelAdmin, self).get_page(request)
        page.body = await self.get_list_table(request)
        return page