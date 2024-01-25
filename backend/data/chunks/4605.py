def test_swagger_ui_html(client: TestClient):
    response = client.get("/docs")
    assert response.status_code == 200, response.text
    assert (
        "https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js" in response.text
    )
    assert "https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css" in response.text