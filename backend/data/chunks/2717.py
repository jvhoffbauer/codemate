def test_delete():
    response = client.request("DELETE", "/items/foo", json={"name": "Foo"})
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "foo", "item": {"name": "Foo", "price": None}}