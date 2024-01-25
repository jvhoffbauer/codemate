async def test_update_fields(
    app: FastAPI, async_client: AsyncClient, fake_users, models
):
    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        update_fields = [models.User.username]

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "password" not in schemas["UserCrudUpdate"]["properties"]
    assert "username" in schemas["UserCrudUpdate"]["properties"]

    # test api
    res = await async_client.put("/user/item/1", json={"username": "new_name"})
    assert res.json()["data"] == 1

    res = await async_client.put("/user/item/1", json={"password": "new_password"})
    assert res.json() == {"detail": "error data handle"}