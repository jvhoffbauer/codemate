def test_no_query():
    client = get_client()
    response = client.post("/items/")
    assert response.status_code == 200
    assert response.json() == "Hello World"