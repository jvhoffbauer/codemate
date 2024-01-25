async def test_list_display(site: AdminSite, async_client: AsyncClient, models):
    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User
        list_display = [models.User.id, models.User.username]

    site.register_router()
    ins = site.get_admin_or_create(UserAdmin)
    assert "username" in model_fields(ins.schema_list)

    # test schemas
    openapi = site.fastapi.openapi()
    schemas = openapi["components"]["schemas"]
    assert "username" in schemas["UserAdminList"]["properties"]