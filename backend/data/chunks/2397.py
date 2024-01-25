def test_route_converters_float():
    # Test float conversion
    response = client.get("/float/25.5")
    assert response.status_code == 200, response.text
    assert response.json() == {"float": 25.5}
    assert app.url_path_for("float_convertor", param=25.5) == "/float/25.5"  # type: ignore