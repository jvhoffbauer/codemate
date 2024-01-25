def test_read_hero_not_found(client: TestClient):
    response = client.get("/heroes/9000")
    assert response.status_code == 404