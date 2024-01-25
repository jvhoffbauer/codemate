def test_root():
    client = get_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}