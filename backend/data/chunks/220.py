def test_update_hero_not_found(client: TestClient):
    response = client.patch("/heroes/9000", json={"name": "Very-Rusty-Man"})
    assert response.status_code == 404