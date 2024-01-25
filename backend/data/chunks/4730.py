def test_disable_openapi(monkeypatch):
    monkeypatch.setenv("OPENAPI_URL", "")
    # Load the client after setting the env var
    client = get_client()
    response = client.get("/openapi.json")
    assert response.status_code == 404, response.text
    response = client.get("/docs")
    assert response.status_code == 404, response.text
    response = client.get("/redoc")
    assert response.status_code == 404, response.text