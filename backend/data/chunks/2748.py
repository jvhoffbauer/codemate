def test_required_noneable_query_value():
    response = client.get("/query", params={"q": "foo"})
    assert response.status_code == 200
    assert response.json() == "foo"