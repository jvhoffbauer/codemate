def test_get_all_job(client: TestClient, superuser_token_headers: dict) -> None:
    response = client.get("/jobs/all", headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert isinstance(response.json()["data"], list)