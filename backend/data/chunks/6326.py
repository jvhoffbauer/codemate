async def test_list_filter(site: AdminSite, async_client: AsyncClient, models):
    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User
        list_filter = [models.User.id, models.User.username.label("name")]
        search_fields = [models.User.username]

    site.register_router()
    ins = site.get_admin_or_create(UserAdmin)
    assert "username" in model_fields(ins.schema_filter)

    # test schemas
    openapi = site.fastapi.openapi()
    schemas = openapi["components"]["schemas"]
    assert "id" in schemas["UserAdminFilter"]["properties"]
    assert "username" in schemas["UserAdminFilter"]["properties"]
    assert "name" in schemas["UserAdminFilter"]["properties"]
    assert "password" not in schemas["UserAdminFilter"]["properties"]