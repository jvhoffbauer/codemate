def test_endpoint_works():
    response = client.post("/", json=[1, 2, 3])
    assert response.json() == 6