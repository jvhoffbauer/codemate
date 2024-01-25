async def test_create_fields(app: FastAPI, async_client: AsyncClient, models):
    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        create_fields = [models.User.username]

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    assert "username" in model_fields(ins.schema_create)
    assert "password" not in model_fields(ins.schema_create)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "username" in schemas["UserCrudCreate"]["properties"]
    assert "password" not in schemas["UserCrudCreate"]["properties"]
    # test api
    body = {"username": "User", "password": "password", "address": [], "attach": {}}
    res = await async_client.post("/user/item", json=body)
    data = res.json().get("data")
    assert data["id"] > 0
    assert data["username"] == "User"
    assert data["password"] == ""