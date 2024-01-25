async def test_list_filter_relationship(
    app: FastAPI, async_client: AsyncClient, fake_articles, models
):
    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"
        list_filter = [
            "id",
            models.Article.title,
            models.User.username,
            models.User.password.label("pwd"),
            LabelField(
                label=models.User.password.label("pwd2"),
                field=Field(None, title="pwd_title"),
            ),
        ]

        async def get_select(self, request: Request) -> Select:
            sel = await super().get_select(request)
            return sel.outerjoin(models.User, models.User.id == models.Article.user_id)

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)
    # test schemas
    assert "title" in model_fields(ins.schema_filter)
    assert "user_username" in model_fields(ins.schema_filter)
    assert "pwd" in model_fields(ins.schema_filter)
    assert "pwd2" in model_fields(ins.schema_filter)
    assert model_fields(ins.schema_filter)["pwd2"].field_info.title == "pwd_title"
    assert "description" not in model_fields(ins.schema_filter)
    # test openapi
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]

    assert "title" in schemas["ArticleCrudFilter"]["properties"]

    assert "user__username" in schemas["ArticleCrudFilter"]["properties"]
    assert "pwd" in schemas["ArticleCrudFilter"]["properties"]
    assert "description" not in schemas["ArticleCrudFilter"]["properties"]

    # test api
    res = await async_client.post("/article/list", json={"id": 2})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 2
    assert "user__username" not in items[0]
    assert "pwd" not in items[0]

    res = await async_client.post("/article/list", json={"user__username": "User_2"})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 2

    res = await async_client.post("/article/list", json={"pwd": "password_2"})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 2

    res = await async_client.post("/article/list", json={"pwd2": "password_2"})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 2