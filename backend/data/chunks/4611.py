def test_swagger_ui_html(client: TestClient):
    response = client.get("/docs")
    assert response.status_code == 200, response.text
    assert "/static/swagger-ui-bundle.js" in response.text
    assert "/static/swagger-ui.css" in response.text