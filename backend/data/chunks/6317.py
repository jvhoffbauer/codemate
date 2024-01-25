    @site.register_admin
    class TmpAdmin(admin.TemplateAdmin):
        page_path = "/index"
        templates = Jinja2Templates(directory=str(tmpdir))
        template_name = "index.html"

        async def get_page(self, request: Request) -> Dict[str, Any]:
            return {"username": "hello"}