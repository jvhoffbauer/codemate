def test_foo_needy_very():
    response = client.get("/items/foo?needy=very")
    assert response.status_code == 200
    assert response.json() == {"item_id": "foo", "needy": "very"}