async def test_list_filter_default(site: AdminSite, async_client: AsyncClient, models):
    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User

    site.register_router()
    ins = site.get_admin_or_create(UserAdmin)
    assert "username" in model_fields(ins.schema_filter)

    # test schemas
    openapi = site.fastapi.openapi()
    schemas = openapi["components"]["schemas"]
    assert "username" in schemas["UserAdminFilter"]["properties"]
    assert "id" in schemas["UserAdminFilter"]["properties"]
    assert "password" in schemas["UserAdminFilter"]["properties"]