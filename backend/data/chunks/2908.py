def test_query_optional():
    response = client.get("/query/optional")
    assert response.status_code == 200
    assert response.json() == "foo bar"