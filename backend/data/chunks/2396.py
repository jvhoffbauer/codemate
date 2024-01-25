def test_route_converters_int():
    # Test integer conversion
    response = client.get("/int/5")
    assert response.status_code == 200, response.text
    assert response.json() == {"int": 5}
    assert app.url_path_for("int_convertor", param=5) == "/int/5"  # type: ignore