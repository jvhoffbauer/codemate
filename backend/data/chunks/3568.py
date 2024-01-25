def test_swagger_ui():
    response = client.get("/docs")
    assert response.status_code == 200, response.text
    print(response.text)
    assert "ui.initOAuth" in response.text
    assert '"appName": "The Predendapp"' in response.text
    assert '"clientId": "the-foo-clients"' in response.text