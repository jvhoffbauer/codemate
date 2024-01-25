    @site.register_admin
    class TmpAdmin(admin.PageAdmin):
        page_path = "/test"

        async def get_page(self, request: Request) -> Page:
            return Page(title="hello", body="Test Amis Page")