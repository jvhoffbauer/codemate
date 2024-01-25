@needs_py310
def test_get_car(client: TestClient):
    response = client.get("/items/item1")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "description": "All my friends drive a low rider",
        "type": "car",
    }