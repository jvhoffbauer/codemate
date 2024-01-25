def test_route_converters_path():
    # Test path conversion
    response = client.get("/path/some/example")
    assert response.status_code == 200, response.text
    assert response.json() == {"path": "some/example"}