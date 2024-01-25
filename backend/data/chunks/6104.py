    async def get_page(self, request: Request) -> Union[Page, App]:
        if self.page_schema.tabsMode is None:
            return await self._get_page_as_app(request)
        return await self._get_page_as_tabs(request)