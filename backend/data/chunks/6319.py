async def test_register_router(site: AdminSite, models):
    site.register_admin(admin.ModelAdmin)
    with pytest.raises(AssertionError) as exc:
        ins = site.get_admin_or_create(admin.ModelAdmin)
    assert exc.match("model is None")
    site.unregister_admin(admin.ModelAdmin)

    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User

    ins = site.get_admin_or_create(UserAdmin)
    assert ins.engine
    assert ins.fields
    site.register_router()
    # test openapi
    openapi = site.fastapi.openapi()
    paths = openapi["paths"]
    assert f"{ins.router_prefix}/list" in paths
    assert f"{ins.router_prefix}/item" in paths
    assert f"{ins.router_prefix}/item/{{item_id}}" in paths