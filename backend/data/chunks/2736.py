def test_swagger_ui_oauth2_redirect():
    response = client.get(swagger_ui_oauth2_redirect_url)
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "window.opener.swaggerUIRedirectOauth2" in response.text