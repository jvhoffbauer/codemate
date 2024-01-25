def test_swagger_ui():
    response = client.get("/docs")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "swagger-ui-dist" in response.text
    print(client.base_url)
    assert (
        f"oauth2RedirectUrl: window.location.origin + '{swagger_ui_oauth2_redirect_url}'"
        in response.text
    )