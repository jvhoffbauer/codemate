async def test_schema_list(app: FastAPI, async_client: AsyncClient, fake_users, models):
    class UserList(BaseModel):
        id: int
        username: str

    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        schema_list = UserList

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "password" not in schemas["UserList"]["properties"]
    assert "username" in schemas["UserList"]["properties"]

    # test api
    res = await async_client.post("/user/list", json={"id": 1})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 1
    assert "username" in items[0]
    assert "password" not in items[0]