async def test_route_list(async_client: AsyncClient, fake_users):
    # list
    res = await async_client.post("/User/list")
    items = res.json()["data"]["items"]
    assert len(items) == 5

    res = await async_client.post("/User/list", json={"id": 1})
    items = res.json()["data"]["items"]
    assert items[0]["id"] == 1
    assert items[0]["username"] == "User_1"
    assert items[0]["address"] == ["address_1", "address_2"]
    assert items[0]["attach"] == {"attach_1": "attach_1", "attach_2": "attach_2"}

    res = await async_client.post("/User/list", json={"username": "User_1"})
    items = res.json()["data"]["items"]
    assert items[0]["username"] == "User_1"

    res = await async_client.post("/User/list", json={"id": "[>]1"})
    assert len(res.json()["data"]["items"]) == 4

    res = await async_client.post("/User/list", json={"id": "[*]1,3"})
    assert len(res.json()["data"]["items"]) == 2

    res = await async_client.post("/User/list", json={"id": "[-]2,3"})
    assert len(res.json()["data"]["items"]) == 2

    res = await async_client.post("/User/list", json={"username": "[~]User_%"})
    assert len(res.json()["data"]["items"]) == 5

    res = await async_client.post(
        "/User/list", json={"create_time": "[-]2022-01-02 00:00:00,2022-01-04 01:00:00"}
    )
    assert len(res.json()["data"]["items"]) == 3