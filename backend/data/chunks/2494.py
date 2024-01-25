@needs_pydanticv2
def test_get(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {"width": 3, "length": 4, "area": 12}