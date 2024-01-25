async def test_schema_read(app: FastAPI, async_client: AsyncClient, fake_users, models):
    class UserRead(ORMModelMixin):
        id: int
        username: str

    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        schema_read = UserRead

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "password" not in schemas["UserRead"]["properties"]
    assert "username" in schemas["UserRead"]["properties"]

    # test api
    res = await async_client.get("/user/item/1")
    items = res.json()["data"]
    assert items["id"] == 1
    assert "username" in items
    assert "password" not in items