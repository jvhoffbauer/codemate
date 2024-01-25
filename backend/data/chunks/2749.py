def test_required_nonable_explicit_query_invalid():
    response = client.get("/explicit-query")
    assert response.status_code == 422