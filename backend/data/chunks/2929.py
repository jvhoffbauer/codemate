def test_query_frozenset_query_1_query_1_query_2():
    response = client.get("/query/frozenset/?query=1&query=1&query=2")
    assert response.status_code == 200
    assert response.json() == "1,2"