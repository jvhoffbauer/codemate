async def test_TemplateAdmin(site: AdminSite, async_client: AsyncClient, tmpdir):
    path = os.path.join(tmpdir, "index.html")
    with open(path, "w") as file:
        file.write("<html>Hello,{{ username }}</html>")

    @site.register_admin
    class TmpAdmin(admin.TemplateAdmin):
        page_path = "/index"
        templates = Jinja2Templates(directory=str(tmpdir))
        template_name = "index.html"

        async def get_page(self, request: Request) -> Dict[str, Any]:
            return {"username": "hello"}

    ins = site.get_admin_or_create(TmpAdmin)
    assert ins.page_path == "/index"
    assert ins.page_schema.url == ins.router_path + ins.page_path
    assert (
        isinstance(ins.page_schema.schema_, amis.Iframe)
        and ins.page_schema.schema_.src == ins.page_schema.url
    )
    site.register_router()

    # test jinja2 html
    res = await async_client.get(ins.router_path + ins.page_path)
    assert res.text == "<html>Hello,hello</html>"