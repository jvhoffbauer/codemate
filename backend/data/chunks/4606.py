def test_swagger_ui_oauth2_redirect_html(client: TestClient):
    response = client.get("/docs/oauth2-redirect")
    assert response.status_code == 200, response.text
    assert "window.opener.swaggerUIRedirectOauth2" in response.text