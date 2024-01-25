async def test_route_update(async_client: AsyncClient, fake_users, models):
    # update one
    res = await async_client.put(
        "/User/item/1",
        json={
            "username": "new_name",
            "address": ["address_3"],
            "attach": {"attach_3": "attach_3"},
        },
    )
    count = res.json()["data"]
    assert count == 1
    user = await db.session.get(models.User, 1)
    assert user.username == "new_name"
    assert user.address == ["address_3"]
    assert user.attach == {"attach_3": "attach_3"}
    # update bulk
    res = await async_client.put(
        "/User/item/1,2,4",
        json={
            "password": "new_password",
            "address": ["address_3"],
            "attach": {"attach_3": "attach_3"},
        },
    )
    count = res.json()["data"]
    assert count == 3
    db.session.expire_all()
    for user in await db.session.scalars(
        select(models.User).where(models.User.id.in_([1, 2, 4]))
    ):
        assert user.password == "new_password"
        assert user.address == ["address_3"]
        assert user.attach == {"attach_3": "attach_3"}