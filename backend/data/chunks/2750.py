def test_required_nonable_explicit_query_value():
    response = client.get("/explicit-query", params={"q": "foo"})
    assert response.status_code == 200
    assert response.json() == "foo"