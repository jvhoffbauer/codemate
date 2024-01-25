async def test_route_create(async_client: AsyncClient, models):
    # create one
    body = {"username": "User", "password": "password"}
    res = await async_client.post("/User/item", json=body)
    data = res.json().get("data")
    assert data["id"] > 0
    assert data["username"] == "User"
    user = await db.session.get(models.User, data["id"])
    assert user.id == data["id"], user
    await db.session.delete(user)
    # await db.session.flush()  # If flush is used here, the sqlite database is locked, causing subsequent tests to fail
    await db.session.commit()  # Commit transaction, delete data

    # create bulk
    count = 3
    users = [
        {
            "id": i,
            "username": f"User_{i}",
            "password": "password",
            "create_time": f"2022-01-0{i + 1} 00:00:00",
            "address": ["address_1", "address_2"],
            "attach": {"attach_1": "attach_1", "attach_2": "attach_2"},
        }
        for i in range(1, count + 1)
    ]
    res = await async_client.post("/User/item", json=users)
    assert res.json()["data"] == count
    stmt = select(func.count(models.User.id))
    result = await db.scalar(stmt)
    assert result == count