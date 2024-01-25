def test_query_optional_not_declared_baz():
    response = client.get("/query/optional?not_declared=baz")
    assert response.status_code == 200
    assert response.json() == "foo bar"