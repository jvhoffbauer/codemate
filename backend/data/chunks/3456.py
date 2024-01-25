def test_hidden_path():
    client = TestClient(app)
    response = client.get("/hidden_path/hidden_path")
    assert response.status_code == 200
    assert response.json() == {"hidden_path": "hidden_path"}