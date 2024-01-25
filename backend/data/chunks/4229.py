def test_get_item_not_found_header():
    response = client.get("/items-header/bar")
    assert response.status_code == 404, response.text
    assert response.headers.get("x-error") == "There goes my error"
    assert response.json() == {"detail": "Item not found"}