async def test_schema_create(app: FastAPI, async_client: AsyncClient, models):
    class UserCreate(BaseModel):
        username: str

    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        schema_create = UserCreate

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)

    assert "username" in model_fields(ins.schema_create)
    assert "password" not in model_fields(ins.schema_create)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "username" in schemas["UserCreate"]["properties"]
    assert "password" not in schemas["UserCreate"]["properties"]
    # test api
    body = {"username": "User", "password": "password"}
    res = await async_client.post("/user/item", json=body)
    data = res.json().get("data")
    assert data["id"] > 0
    assert data["username"] == "User"
    assert data["password"] == ""