    async def get_page(self, request: Request) -> Page:
        return self.page or Page()