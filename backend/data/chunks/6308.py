async def test_RouterAdmin(site: AdminSite, async_client: AsyncClient):
    @site.register_admin
    class TmpAdmin(admin.RouterAdmin):
        router_prefix = "/router"

        def register_router(self):
            @self.router.get("/hello")
            def hello():
                return {"username": "hello"}

    ins = site.get_admin_or_create(TmpAdmin)
    assert ins.router_path == f"{site.settings.site_path}/router"

    site.register_router()
    res = await async_client.get("/router/hello")
    assert res.json() == {"username": "hello"}