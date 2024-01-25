def test_openapi_schema():
    with pytest.raises(ValueError):
        client.get("/openapi.json")