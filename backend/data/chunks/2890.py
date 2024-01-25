def test_get_item_1():
    """Check that /items/{item_id} returns expected data"""
    response = client.get("/items/item01")
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "item01"}