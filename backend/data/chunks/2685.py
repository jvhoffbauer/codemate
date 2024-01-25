def test_put_no_body():
    response = client.put("/items/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "foo"}