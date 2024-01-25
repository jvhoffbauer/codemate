async def test_route_read(async_client: AsyncClient, fake_users):
    # read one
    res = await async_client.get("/User/item/1")
    user = res.json()["data"]
    assert user["id"] == 1
    assert user["username"] == "User_1"
    assert user["address"] == ["address_1", "address_2"]
    assert user["attach"] == {"attach_1": "attach_1", "attach_2": "attach_2"}
    # read bulk
    res = await async_client.get("/User/item/1,2,4")
    users = res.json()["data"]
    assert len(users) == 3
    assert users[0]["username"] == "User_1"
    assert users[2]["username"] == "User_4"
    assert users[0]["address"] == ["address_1", "address_2"]
    assert users[2]["address"] == ["address_1", "address_2"]