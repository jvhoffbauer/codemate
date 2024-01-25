def test_add_job(
    client: TestClient, job_id: str, superuser_token_headers: dict
) -> None:
    response = client.post(
        "/job/schedule",
        json={"seconds": 5, "job_id": job_id},
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["data"]["id"] == job_id