async def test_schema_filter(
    app: FastAPI, async_client: AsyncClient, fake_users, models
):
    class UserFilter(BaseModel):
        id: int = None
        username: str = None

    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        schema_filter = UserFilter

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "password" not in schemas["UserFilter"]["properties"]
    assert "username" in schemas["UserFilter"]["properties"]

    # test api
    res = await async_client.post("/user/list", json={"id": 1})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 1

    res = await async_client.post("/user/list", json={"username": "User_1"})
    items = res.json()["data"]["items"]
    assert items[0]["username"] == "User_1"

    res = await async_client.post("/user/list", json={"password": "new_password"})
    items = res.json()["data"]["items"]
    assert items