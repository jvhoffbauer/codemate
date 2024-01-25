async def test_PageAdmin(site: AdminSite, async_client: AsyncClient):
    @site.register_admin
    class TmpAdmin(admin.PageAdmin):
        page_path = "/test"

        async def get_page(self, request: Request) -> Page:
            return Page(title="hello", body="Test Amis Page")

    ins = site.get_admin_or_create(TmpAdmin)
    assert ins.page_path == "/test"
    assert ins.page_schema.url == ins.router_path + ins.page_path

    site.register_router()
    # test amis json
    res = await async_client.post(ins.router_path + ins.page_path)
    assert res.json()["data"] == {
        "type": "page",
        "title": "hello",
        "body": "Test Amis Page",
    }
    # test amis html
    res = await async_client.get(ins.router_path + ins.page_path)
    assert res.text.find(Page(title="hello", body="Test Amis Page").amis_json())
    # test amis json _update
    res = await async_client.post(
        ins.router_path + ins.page_path,
        json={"_update": {"title": "new title", "extra": "extra data"}},
    )
    assert res.json()["data"] == {
        "type": "page",
        "title": "new title",
        "body": "Test Amis Page",
        "extra": "extra data",
    }