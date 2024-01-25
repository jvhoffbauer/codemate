async def test_pk_name(app: FastAPI, async_client: AsyncClient, fake_users, models):
    class UserCrud(SqlalchemyCrud):
        router_prefix = "/user"
        pk_name = "username"
        read_fields = [models.User.id, models.User.username, models.User.password]

    ins = UserCrud(models.User, db.engine).register_crud()

    app.include_router(ins.router)
    assert ins.pk.key == "username"
    # read one
    res = await async_client.get("/user/item/User_1")
    user = res.json()["data"]
    assert user["id"] == 1
    assert user["username"] == "User_1"
    # read bulk
    res = await async_client.get("/user/item/User_1,User_2,User_4")
    users = res.json()["data"]
    assert len(users) == 3
    assert users[0]["username"] == "User_1"
    assert users[2]["username"] == "User_4"