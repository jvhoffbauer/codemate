def test_get_starlette_item_not_found():
    response = client.get("/starlette-items/bar")
    assert response.status_code == 404, response.text
    assert response.headers.get("x-error") is None
    assert response.json() == {"detail": "Item not found"}