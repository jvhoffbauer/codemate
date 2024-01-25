def test_query_query_baz():
    response = client.get("/query?query=baz")
    assert response.status_code == 200
    assert response.json() == "foo bar baz"