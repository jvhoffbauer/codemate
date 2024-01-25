async def test_route_delete(async_client: AsyncClient, fake_users, models):
    # delete one
    res = await async_client.delete("/User/item/1")
    count = res.json()["data"]
    assert count == 1
    user = await db.get(models.User, 1)
    assert user is None
    # delete bulk
    res = await async_client.delete("/User/item/2,4")
    count = res.json()["data"]
    assert count == 2
    assert await db.get(models.User, 2) is None
    assert await db.get(models.User, 4) is None