def test_query_param():
    response = client.get("/query/param")
    assert response.status_code == 200
    assert response.json() == "foo bar"