def test_route_converters_query():
    # Test query conversion
    response = client.get("/query", params={"param": "Qué tal!"})
    assert response.status_code == 200, response.text
    assert response.json() == {"query": "Qué tal!"}