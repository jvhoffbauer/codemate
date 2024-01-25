def test_root_token_jessica(client: TestClient):
    response = client.get("/?token=jessica")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}