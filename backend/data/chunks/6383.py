def test_route_delete(client: TestClient, fake_users, models):
    # delete one
    res = client.delete("/User/item/1")
    count = res.json()["data"]
    assert count == 1
    user = db.get(models.User, 1)
    assert user is None
    # delete bulk
    res = client.delete("/User/item/2,4")
    count = res.json()["data"]
    assert count == 2
    assert db.get(models.User, 2) is None
    assert db.get(models.User, 4) is None