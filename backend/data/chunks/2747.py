def test_required_nonable_query_invalid():
    response = client.get("/query")
    assert response.status_code == 422