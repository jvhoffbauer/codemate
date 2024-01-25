def test_route_create(client: TestClient, models):
    # create one
    body = {"username": "create", "password": "password"}
    res = client.post("/User/item", json=body)
    data = res.json().get("data")
    assert data["id"] > 0
    assert data["username"] == "create"
    user = db.session.get(models.User, data["id"])
    assert user.id == data["id"], user
    db.session.delete(user)
    db.session.commit()
    # create bulk
    count = 3
    users = [
        {
            "id": i,
            "username": f"create_{i}",
            "password": "password",
            "create_time": f"2022-01-0{i + 1} 00:00:00",
        }
        for i in range(1, count + 1)
    ]
    res = client.post("/User/item", json=users)
    assert res.json()["data"] == count
    stmt = select(func.count(models.User.id))
    user = db.session.scalar(stmt)
    assert user == count