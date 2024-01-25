def test_swagger_ui_no_oauth2_redirect():
    response = client.get("/docs/oauth2-redirect")
    assert response.status_code == 404, response.text