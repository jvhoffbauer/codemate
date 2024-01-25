def test_delete_hero_not_found(client: TestClient):
    response = client.delete("/heroes/9000")
    assert response.status_code == 404