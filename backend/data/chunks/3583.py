def test_get_item_not_found():
    response = client.get("/items/bar")
    assert response.status_code == 404, response.text
    assert response.headers.get("x-error") == "Some custom header"
    assert response.json() == {"detail": "Item not found"}