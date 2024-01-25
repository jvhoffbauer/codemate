def test_custom_response_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json()["components"]["schemas"]["Item"] == item_schema