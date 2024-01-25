def test_get_valid():
    response = client.get("/foo", params={"client_id": "bar"})
    assert response.status_code == 200
    assert response.json() == {"client_id": "bar_key", "client_tag": "bar_tag"}