def test_get_parameters():
    response = client.get("/test_path", params={"repeated_alias": "test_query"})
    assert response.status_code == 200, response.text
    assert response.json() == {"path": "test_path", "query": "test_query"}