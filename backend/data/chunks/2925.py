def test_query_param_required_query_50():
    response = client.get("/query/param-required?query=50")
    assert response.status_code == 200
    assert response.json() == "foo bar 50"