def test_openapi_schema_sub():
    response = client.get("/subapi/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == openapi_schema_sub