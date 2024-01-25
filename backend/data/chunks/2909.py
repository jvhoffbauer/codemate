def test_query_optional_query_baz():
    response = client.get("/query/optional?query=baz")
    assert response.status_code == 200
    assert response.json() == "foo bar baz"