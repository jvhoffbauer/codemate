def test_route_update(client: TestClient, fake_users, models):
    # update one
    res = client.put("/User/item/1", json={"username": "new_name"})
    count = res.json()["data"]
    assert count == 1
    user = db.session.get(models.User, 1)
    assert user.username == "new_name"
    # update bulk
    res = client.put("/User/item/1,2,4", json={"password": "new_password"})
    count = res.json()["data"]
    assert count == 3
    db.session.expire_all()  # Make the instance expire, because when creating the user,
    # the user object attributes have been cached, so you need to expire.
    for user in db.session.scalars(
        select(models.User).where(models.User.id.in_([1, 2, 4]))
    ):
        assert user.password == "new_password"