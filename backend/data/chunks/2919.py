def test_query_int_default():
    response = client.get("/query/int/default")
    assert response.status_code == 200
    assert response.json() == "foo bar 10"