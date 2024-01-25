def test_call_valid():
    response = client.post("/", json={})
    assert response.status_code == 200
    assert response.json() == {}