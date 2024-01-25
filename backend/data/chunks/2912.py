def test_query_int_query_42():
    response = client.get("/query/int?query=42")
    assert response.status_code == 200
    assert response.json() == "foo bar 42"