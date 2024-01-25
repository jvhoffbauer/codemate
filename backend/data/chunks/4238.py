def test_post():
    data = {"title": "towel", "size": 5}
    response = client.post("/items/", json=data)
    assert response.status_code == 200, response.text
    assert response.json() == data