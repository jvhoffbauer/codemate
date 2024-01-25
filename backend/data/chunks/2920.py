def test_query_int_default_query_50():
    response = client.get("/query/int/default?query=50")
    assert response.status_code == 200
    assert response.json() == "foo bar 50"