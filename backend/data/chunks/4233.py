def test_get():
    response = client.get("/items/2")
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": 2}