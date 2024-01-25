async def test_list_display_join(site: AdminSite, async_client: AsyncClient, models):
    @site.register_admin
    class ArticleAdmin(admin.ModelAdmin):
        model = models.Article
        list_display = [
            models.Article.title,
            models.User.username,
            "description",
            models.User.username.label("nickname"),
            LabelField(
                label=models.User.password.label("pwd"),
                field=Field(None, title="pwd_title"),
            ),
        ]

        async def get_select(self, request: Request) -> Select:
            sel = await super().get_select(request)
            return sel.outerjoin(models.User, models.User.id == models.Article.user_id)

    site.register_router()

    ins = site.get_admin_or_create(ArticleAdmin)
    # test schemas
    assert "id" in model_fields(ins.schema_list)
    assert "user_username" in model_fields(ins.schema_list)
    assert "description" in model_fields(ins.schema_list)
    assert "nickname" in model_fields(ins.schema_list)
    assert "pwd" in model_fields(ins.schema_list)
    assert model_fields(ins.schema_list)["pwd"].field_info.title == "pwd_title"

    assert "user_username" in model_fields(ins.schema_filter)
    assert "nickname" in model_fields(ins.schema_filter)
    assert "pwd" in model_fields(ins.schema_filter)

    # test openapi
    site.fastapi.openapi_schema = None
    openapi = site.fastapi.openapi()
    schemas = openapi["components"]["schemas"]
    assert "user__username" in schemas["ArticleAdminList"]["properties"]
    assert "description" in schemas["ArticleAdminList"]["properties"]
    assert "nickname" in schemas["ArticleAdminList"]["properties"]
    assert "pwd" in schemas["ArticleAdminList"]["properties"]