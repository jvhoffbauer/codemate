def test_put_no_body_with_body():
    response = client.put("/items/foo", json={"name": "Foo"})
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "foo"}