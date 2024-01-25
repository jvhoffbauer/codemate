    async def _get_page_as_tabs(self, request: Request) -> Page:
        page = await super(AdminApp, self).get_page(request)
        children = await self.get_page_schema_children(request)
        page.body = PageSchema(
            children=children, tabsMode=self.page_schema.tabsMode
        ).as_page_body()
        return page