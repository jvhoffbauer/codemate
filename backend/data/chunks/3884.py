def test_path_operation_not_found():
    response = client.get("/items/bar")
    assert response.status_code == 404, response.text
    assert response.json() == {"message": "Item not found"}