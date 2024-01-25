def test_query_int_optional():
    response = client.get("/query/int/optional")
    assert response.status_code == 200
    assert response.json() == "foo bar"