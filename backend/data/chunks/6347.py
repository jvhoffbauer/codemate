async def test_schema_update(
    app: FastAPI, async_client: AsyncClient, fake_users, models
):
    class UserUpdate(BaseModel):
        password: str = None

    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        schema_update = UserUpdate

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "password" in schemas["UserUpdate"]["properties"]
    assert "username" not in schemas["UserUpdate"]["properties"]

    # test api
    res = await async_client.put("/user/item/1", json={"username": "new_name"})
    assert res.json() == {"detail": "error data handle"}
    res = await async_client.put("/user/item/1", json={"password": "new_password"})
    assert res.json()["data"] == 1