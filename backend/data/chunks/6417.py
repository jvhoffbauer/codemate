async def test_list_filter(app: FastAPI, async_client: AsyncClient, fake_users, models):
    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        list_filter = [models.User.id, models.User.username]

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    assert "username" in model_fields(ins.schema_filter)
    assert "password" not in model_fields(ins.schema_filter)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "username" in schemas["UserCrudFilter"]["properties"]
    assert "password" not in schemas["UserCrudFilter"]["properties"]

    # test api
    res = await async_client.post("/user/list", json={"id": 2})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 2

    res = await async_client.post("/user/list", json={"username": "User_2"})
    items = res.json()["data"]["items"]
    assert items[0]["username"] == "User_2"

    res = await async_client.post("/user/list", json={"password": "new_password"})
    items = res.json()["data"]["items"]
    assert items